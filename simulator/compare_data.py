import pandas as pd
import numpy as np
import warnings

class CompareData:

    compared_df = None
    match_prefix = '#match_'

    def __init__(self, first_path:str=None, second_path:str=None, file_type:str=None, decimal_match=2, match_case=False):
        self.first_path = first_path
        self.second_path = second_path
        self.file_type = file_type
        self.decimal_match = decimal_match
        self.match_case = match_case



    def readData(self) -> tuple:
        print("Reading files ...")
        if self.file_type == '.csv':
            first_df = pd.read_csv(self.first_path, low_memory=False)
            second_df = pd.read_csv(self.second_path, low_memory=False)
        elif self.file_type == '.xlsx':
            first_df = pd.read_excel(self.first_path)
            second_df = pd.read_excel(self.second_path)
        else:
            raise ValueError("Invalid file_type passed", self.file_type)
        print("Files read successfully ...")
        return first_df, second_df
    


    def summary(self):
        result = {
            'Column_name': [],
            'Percentage_match':[],
            'True_counts': [],
            'False_counts': [],
            'Noise': [],
            'Column_size':[]
            }
        
        for col in self.compared_df.columns:
            if self.match_prefix in col[:len(self.match_prefix)]:
                result['Column_name'].append(col.replace(self.match_prefix, ''))
                result['True_counts'].append(self.compared_df[self.compared_df[col].astype(bool) == True].shape[0])
                result['False_counts'].append(self.compared_df[self.compared_df[col].astype(bool) == False].shape[0])
                result['Percentage_match'].append(round(self.compared_df[self.compared_df[col].astype(bool) == True].shape[0] / self.compared_df[col].shape[0] * 100, 2))
                result['Noise'].append(self.compared_df[~self.compared_df[col].isin([True, False])].shape[0])
                result['Column_size'].append(self.compared_df[col].shape[0])
        
        result_df = pd.DataFrame(result)
        result_df.index = result_df['Column_name']
        result_df = result_df.drop(['Column_name'], axis='columns')
        description = result_df.describe().T.round(self.decimal_match)
        result_df = result_df.T
        result_df = pd.concat([result_df, description], axis='columns')
        return result_df



    def matchCols(self, df1:pd.DataFrame, df2:pd.DataFrame, col:str, primary_key:str):
        df2_data = df1[primary_key].map(df2.set_index(primary_key)[col])
        if df1[col].dtype == float:
            match = np.where(
                        (df1[col].isnull() & df2_data.isnull()), 
                        True,
                np.where((df1[col].round(self.decimal_match) == df2_data.round(self.decimal_match)), 
                        True, 
                        False)
            )

        elif df1[col].dtype == object and self.match_case == False:
            col_1_df = df1[col].astype(str).apply(lambda x: x.lower())
            col_2_df = df2_data.astype(str).apply(lambda x: x.lower())
            match = np.where((col_1_df.isnull() & col_2_df.isnull()), True, np.where((col_1_df == col_2_df), True, False)) 
        else:    
            match = np.where((df1[col].isnull() & df2_data.isnull()), True, np.where((df1[col] == df2_data), True, False)) 
        return df1[col], df2_data, match


    def compareCols(self, primary_key:str, first_df:pd.DataFrame=None, second_df:pd.DataFrame=None):
        if first_df is not None and  second_df is not None:
            pass
        elif self.first_path != None and self.second_path != None:
            first_df, second_df = self.readData()
        else:
            warnings.warn("Provide read paths (first_path and second path) or dataframes (first_df, second_df) to proceed !")
            return 
        
        first_df = first_df.drop_duplicates(subset=primary_key)
        second_df = second_df.drop_duplicates(subset=primary_key)
        common_cols = [col for col in first_df.columns if col in second_df.columns]
        if primary_key in common_cols:
            common_cols.remove(primary_key)
        df = pd.DataFrame()  
        df[primary_key] = first_df[primary_key]
        for col in common_cols:
            print(f"Comparing column {col} ...")
            first_col, second_col, match = self.matchCols(df1=first_df, df2=second_df, 
                                                          col=col, primary_key=primary_key)
            df['first_' + col] = first_col
            df[self.match_prefix + col] = match
            df['second_' + col] = second_col
            df = df.copy()  

        print("Comparison Done ...")
        self.compared_df = df


