import csv
from typing import List, Any


def read_csv(file_name: str) -> List[List[str]]:
    """
    Read data from a CSV file and return it as a list of rows.
    
    Args:
        file_name: Path to the CSV file
        
    Returns:
        List of rows from the CSV file
    """
    data = []
    with open(file_name, 'r', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def filter_by_column(data: List[List[Any]], index: int, value: Any) -> List[List[Any]]:
    """
    Filter rows by matching a value in a specific column.
    
    Args:
        data: List of rows to filter
        index: Column index to check
        value: Value to match
        
    Returns:
        Filtered list of rows
    """
    return [row for row in data if row[index] == value]


def main() -> None:
    """
    Main function to demonstrate CSV reading and filtering.
    """
    data = read_csv('sales.csv')
    filtered = filter_by_column(data, 2, 'Books')
    print("Filtered Data:")
    for row in filtered:
        print(row)


if __name__ == "__main__":
    main()