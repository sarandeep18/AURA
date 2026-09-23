"""
Description:
Provides product recommendations based on similar product
characteristics in the dataset.
Concepts used:
1. Filtering
Used to find products matching selected characteristics.

2. Boolean Conditions
Used to compare values such as Category and Brand.

3. DataFrame Filtering
Used to retrieve matching products from the dataset.
example :
dataset[condition]
dataset[dataset["Category"] == "Electronics"]
It means give me only the rows where Category is Electronics
Simple definition:-
Here we are going to find products similar to the
one selected by the user.
"""
def content_based(dataset, product_name):
    try:
        #Find the selected product
        selected_product = dataset[dataset["Product_Name"] == product_name]
        if selected_product.empty:
            print("Product not found.")
            return dataset
        #Get the category of the selected product
        category = selected_product.iloc[0]["Category"]
        #Find products from the same category
        recommendations = dataset[dataset["Category"] == category]
        print("Recommended Products:")
        print(recommendations)
        return dataset
    except Exception as recommendation_error:
        print("Unable to generate recommendations")
        print(recommendation_error)
        return None