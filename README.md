# Simulator

## Overview

`simulator` is a Python package designed to compare two CSV or Excel files by analyzing their common columns. Additionally, it includes functionalities for JSON operations and API interactions. The package provides structured comparison and analytical insights on the differences between files and supports JSON manipulations.

## Features

- Compare two CSV or Excel files based on common columns.
- Compare two Pandas DataFrames.
- Store the comparison result in the class variable `compared_df`.
- Generate an analysis of the comparison based on:
- Generate a summary of the comparison using `comparator.summary()`, which includes:
  - `Percentage_match`
  - `True_counts`
  - `False_counts`
  - `Noise`
  - `Column_size`
- JSON operations, including:
  - Reading values from JSON paths
  - Updating JSON paths
  - Creating new JSON paths
  - Modifying JSON values based on reference
- API request handling for JSON-based requests.

## Installation

```sh
pip install simulator
```

## Usage

### Import the Package

```python
from simulator import CompareData, JsonOperations, Simulation
```

### Compare Two CSV/Excel Files

```python
# Create an instance of CompareData
comparator = CompareData(first_path='file1.csv', second_path='file2.csv', file_type='csv', decimal_match=2, match_case=False)

# Access the compared dataframe
print(comparator.compared_df)
```

**Explanation:** This function loads two CSV or Excel files and compares them based on common columns.

### Get Comparison Summary

```python
summary = comparator.summary()
print(summary)
```

**Explanation:** This function returns a summary of the comparison, including percentage match, true counts, false counts, noise, and column size.

### Compare Two Pandas DataFrames

```python
comparator = CompareData(decimal_match=0)
comparator.compareCols(primary_key='appID', first_df=first_df, second_df=second_df)
```

**Explanation:** This function allows direct comparison between two Pandas DataFrames based on a primary key.

### API Request Handling

```python
URL = "http://your-api-endpoint.com"
simulator = Simulation(api_url=URL)

# Simulator will send JSON requests and return the JSON response
response = simulator.sendRequest(payload={"key": "value"})
print(response)
```

**Explanation:** This function enables sending API requests and retrieving JSON responses from a given URL.

### JSON Operations

```python
json_operator = JsonOperations()

# Update a JSON path
output_body = json_operator.updatePath(input_body, 'existing_path', "update_value")
```

**Explanation:** Updates a specific JSON path with a new value.

```python
# Create a new JSON path
output_body = json_operator.createPath(input_body, 'new_body_path', "new_value")
```

**Explanation:** Creates a new path in the JSON structure and assigns a value.

```python
# Read a value from a JSON path
read_value = json_operator.readPath(input_body, 'existing_path')
```

**Explanation:** Reads a value from an existing JSON path.

```python
# Modify JSON values by reference
output_json = json_operator.chageByReference(destination_body, reference_body, 'destination_path', 'reference_path')
```

**Explanation:** Changes a JSON value by referencing another JSON object.

## Repository

For more details, visit the GitHub repository:
[simulator on GitHub](https://github.com/Vijay-Takbhate-incred/simulator.git)

## License

This project is licensed under the MIT License.

## Author

[Vijay Takbhate](https://github.com/Vijay-Takbhate-incred)

