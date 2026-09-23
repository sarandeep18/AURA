"""
Description :
Finds the maximum value of a numeric column.
Concepts used:
1. max()
Returns the largest value in a numeric column.

Example:
   dataset["Price"].max()
Simple Definition:
Ur researching whats the expensive product ur gf can ask
"""
def maximum(dataset):
    try:
        maximum_value = dataset["Price"].max()
        print(f"Maximum Price : {maximum_value}")
        return dataset
    except Exception as maximum_error:
        print("Price is hiked and salary is negative")
        print(maximum_error)
        return None