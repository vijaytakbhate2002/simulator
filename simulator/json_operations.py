import pandas as pd
import numpy as np
import json

class JsonOperations:

    def isIndexFromPath(self, key):
        if '[' not in key:
            return key, None
        else:
            res = key.replace('[', ';').replace(']', ';')
            res = res.split(';')
            return res[0], int(res[-2])

    def readPath(self, input_body:dict, read_path:str):
        """ input_body: input json or dict
            read_path: the path you want to read value from
            
            Return: Return value associated with read_path"""
        read_path = read_path.replace('"]', '')
        read_path = read_path.replace('["', '.')
        
        if isinstance(read_path, str):
            read_path = read_path.split(".")

        current = input_body
        for key in read_path[:-1]: 
            key, path_idx = self.isIndexFromPath(key) 
            if path_idx != None and key in current.keys():
                if len(current[key]) - 1 < path_idx:
                    print(f"Returning input body without deletion due to specified path index {path_idx} is out of range {len(current[key])}...")
                    return input_body
                current = current[key][path_idx]
            elif path_idx == None and key in current.keys():
                current = current[key]
            else:
                print("Provided variable path is not found returning None...")
                return None
                
        return current[read_path[-1]]
    
    def deletePath(self, input_body:dict, delete_path:str):
        """ input_body: input json or dict
            delete_path: the path you want to delete
            
            Return: Return dict after deletion of the delete_path (eg. MODEL.BANKING_V2.prediction1)"""
        if isinstance(delete_path, str):
            delete_path = delete_path.split(".")

        current = input_body
        for key in delete_path[:-1]: 
            key, path_idx = self.isIndexFromPath(key) 
            if path_idx != None and key in current.keys():
                if len(current[key]) - 1 < path_idx:
                    print(f"Returning input body without deletion due to specified path index {path_idx} is out of range {len(current[key])}...")
                    return input_body
                current = current[key][path_idx]
            elif path_idx == None and key in current.keys():
                current = current[key]
            else:
                print("Provided variable path is not found returning body", key)
                return input_body
                
        del current[delete_path[-1]]
        return input_body

    def updatePath(self, input_body:dict, update_path:str, update_value) -> dict:
        """ input_body: input json or dict
            update_path: the path you want to update the value for
            update_value: update path will contain update_value (eg. CUST_ID: '123456789C')
            
            Return: Return the updated JSON or dict """
        if isinstance(update_path, str):
            update_path = update_path.split(".") 

        current = input_body
        for key in update_path[:-1]: 
            key, path_idx = self.isIndexFromPath(key) 
            if path_idx != None and key in current.keys():
                if len(current[key]) - 1 < path_idx:
                    return input_body
                current = current[key][path_idx]
            elif path_idx == None and key in current.keys():
                current = current[key]
            else:
                print(f"Provided variable path for {key} is not found returning input_body...")
                return input_body
        if update_path[-1] in current.keys():
            current[update_path[-1]] = update_value  
            return input_body
        else:
            print(f"Does not found key {update_path[-1]} at {'.'.join(update_path[:-1])}...")
            return input_body
        return input_body

    def createPath(self, input_body: dict, create_path: str, update_value: bool = None) -> dict:
        """input_body: input json or dict
            create_path: the path you want to create in json for value insertion
            update_value: the data which you want to assign to create_path 
            
            Return: return JSON / dict with new path and value assigned to it"""
        if isinstance(create_path, str):
            create_path = create_path.split(".")

        current = input_body
        for key in create_path[:-1]:  
            key, path_idx = self.isIndexFromPath(key)
            if path_idx is not None:
                if key not in current and isinstance(current[key], list):
                    current[key] = []
                while len(current[key]) <= path_idx:  
                    current[key].append({})
                current = current[key][path_idx]
            else:
                if key not in current and isinstance(current[key], dict):
                    current[key] = {}  
                current = current[key]
        current[create_path[-1]] = update_value

        return input_body     


    def chageByReference(self, destination_body:dict, reference_body:dict, destination_path:str, reference_path:str) -> dict:
        """ destination_body: The JSON or dict in which you want to change value by refering destination_path
            reference_body: The JSON or dict from which you want to read value to update into  destination_body
            destination_path: JSON or dict path to update value from 
            reference_path : JSON or dict path to read value from 

            Return: return updated JSON

            Working: This function takes 'destination_body' which means the JSON body or dict that you want to change value from 
                     'destination_path'.
                     'reference_body' is a reference JSON or dict for reading content from 'reference_path' to put that into 'destination_body'
        """
        read_value = self.readPath(input_body=reference_body, read_path=reference_path)
        updated_json = self.updatePath(input_body=destination_body, update_path=destination_path, update_value=read_value)
        return updated_json
        
