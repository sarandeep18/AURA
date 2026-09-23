"""
Description:
Recommends products from a selected product's category.
Concepts Used:
1. Boolean Filtering
Used to find products belonging to a category.
2. DataFrame Filtering
Used to retrieve products matching the category.
3. unique()
Used to identify available categories.
Simple Definition:
Here we are recommending products from the same category.
"""
def category_recommendation(dataset, product_name):
    try:
        #Find the selected product
        selected_product = dataset[dataset["Product_Name"] == product_name]
        if selected_product.empty:
            print("Product not found.")
            return dataset
        #Get the category of the selected product
        category = selected_product.iloc[0]["Category"]
        #Find products from the same category
        recommendations = dataset[(dataset["Category"] == category) & (dataset["Product_Name"] != product_name)]
        print("Category Based Recommendations:")
        print(recommendations)
        return dataset
    except Exception as category_recommendation_error:
        print("Unable to generate category recommendations.")
        print(category_recommendation_error)
        return None