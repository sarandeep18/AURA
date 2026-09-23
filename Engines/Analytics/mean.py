"""
Description: Calculates the average value of a numeric column in the dataset.
Concepts used:
1. mean()
   - Returns the average value of a numeric column.
   Example:
   dataset["Price"].mean()
   Output:
   1850.75
Real-life Example:
Here we are going to calculate the average value.

Just like before buying a product,
we compare different prices and think about the average price.

Similarly, we calculate the average value of a column
using the mean() function.
"""
def mean(dataset):
    try:
        #Calculating the average value
        #Just like finding the average budget for impressing your crush
        average_price = dataset["Price"].mean()
        print(f"Average Price: {average_price}")
        return dataset
    except Exception as mean_value_error:
        print("Unable to calculate the average value.")
        print(mean_value_error)
        return None