"""
Description:
Finds products with the highest sales in the dataset and trears them as trending products.
Concepts Used:
1.sort_values()
Sorts the dataset based on a selected column
2.ascending
Controls the sorting order.
False sorts from highest to lowest.
3.head()
Selects the top records after sorting.
Simple Definition:
Here we are finding which products are getting
the most attention.
Basically, checking who is currently trending
instead of asking who was famous last year. 
"""
def trending_products(dataset):
    try:
        #Sorts products based on sales
        #Highest sales come first
        trending_products = dataset.sort_values(by = "Sales", ascending = False)
        #Display top 5 trending products
        print("Trending Products:")
        print(trending_products[["Product_Name","Sales"]].head())
        return dataset
    except Exception as trending_product_error:
        print("Unable to find trending products.")
        print(trending_product_error)
        return None