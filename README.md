# Simulator

## Overview
`simulator` is a Python package designed to compare two CSV or Excel files by analyzing their common columns. The package provides a structured comparison and generates analytical insights on the differences between the files.

## Features
- Compare two CSV or Excel files based on common columns.
- Store the comparison result in the class variable `compared_df`.
- Generate an analysis of the comparison based on:
  - `Percentage_match`
  - `True_counts`
  - `False_counts`
  - `Noise`
  - `Column_size`

## Installation
```sh
pip install simulator
```

## Usage

### Import the package
```python
from simulator import compareData
```

### Compare two CSV/Excel files
```python
# Create an instance of compareData
comparator = compareData('file1.csv', 'file2.csv')

# Access the compared dataframe
print(comparator.compared_df)
```

### Get Comparison Summary
```python
summary = comparator.summary()
print(summary)
```

## Repository
For more details, visit the GitHub repository:
[simulator on GitHub](https://github.com/Vijay-Takbhate-incred/simulator.git)

## License
This project is licensed under the MIT License.

## Author
[Vijay Takbhate](https://github.com/Vijay-Takbhate-incred)

