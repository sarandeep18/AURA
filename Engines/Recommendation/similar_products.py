"""
Description:
Finds products that are similar to a selected product based on its category and brand
Concepts Used:
1.Boolean FIltering:
Used to compare product attributes.
2. DataFrame Filtering
Used to retrieve products matching the conditions.
3. iloc[]
used to access the selected product's row.
Here we are finding products similar to the selected one.
"""
def similar_products(dataset, product_name):
    try:
        #Find the selected product
        selected_product = dataset[dataset["Product_Name"] == product_name]
        if selected_product.empty:
            print("Product not found")
            return dataset
        #Get category and brand of the selected product
        category = selected_product.iloc[0]["Category"]
        brand = selected_product.iloc[0]["Brand"]
        #Find products with the same category and brand
        recommendations = dataset[(dataset["Category"]== category)& (dataset["Brand"] == brand)& (dataset["Product_Name"]!= product_name)]
        print("Similar Products:")
        print(recommendations)
        return dataset
    except Exception as similar_product_error:
        print("Unable to find similar products.")
        print(similar_product_error)
        return None