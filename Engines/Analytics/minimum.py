"""
Description:
Finds the minimum value of a numeric column.
Concepts used:
1. min()
Returns the smallest value in a numeric column
Example:
dataset["Price"].min()
Simple Definition:
It is like searching for the cheapest product
"""
def minimum(dataset):
    try:
        minimum_price = dataset["Price"].min()
        print(f"Minimum Price : {minimum_price}")
        return dataset
    except Exception as minimum_error:
        print("Unable to find minimum value")
        print(minimum_error)
        return None