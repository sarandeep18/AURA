"""
1.dtypes-
    - Returns the data type of each column in the dataset.
Example:
dataset.dtypes
Output:
Product_Name      object
Brand             object
Price             int64
Rating            float64
Discount          float64
float64- Rating = 4.5, Discount = 15.75
int64- Price = 1200, Quantity = 5
object- Product Name,Brand,Category
Here we are going to identify the data type of each column in the dataset.
"""
def data_types(dataset):
    try:
        #Displaying the data type of each column
        #Just like how you identify the type of your crush personality
        print(dataset.dtypes)
        return dataset
    except Exception as data_types_error:
        print("Unable to display the data types.")
        print(data_types_error)
        return None