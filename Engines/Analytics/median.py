"""
Description:
    Calculates the median value of a numeric column
Concepts used:
1. Median()
   - Returns the median value of a numeric column.
   Example:
   dataset["Price"].median()
Simple definition:
The median choose middle value from a dataset."""
def median(dataset):
    try:
        median_ = dataset["Price"].median()
        print(f"Median Price: {median_}")
        return dataset
    except Exception as median_error:
        print("Median calculation failed")
        print(median_error)
        return None