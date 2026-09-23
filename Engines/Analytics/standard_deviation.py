"""
Description:
Calculates the standard deviation of a numeric column
Concepts used:
1.std()
Returns the standard deviation of a numeric column
Example:
dataset["Price"].std()
Simple Definition:
Just like checking whether everyone's marks
are almost the same or very different,
std() tells us how spread out the data is.
"""
def standard_deviation(dataset):
    try:
        standard_deviation_price = dataset["Price"].std()
        print(f"Standard Deviation : {standard_deviation_price}")
        return dataset
    except Exception as standard_deviation_error:
        print("unable to calculate the standard deviation.")
        print(standard_deviation_error)
        return None