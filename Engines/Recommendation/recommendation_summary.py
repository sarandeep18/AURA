"""
Description :
Provides a summary of the generated product recommendations.
Concepts Used:
1. len()
Used to count the number of recommendations.
2. DataFrame Columns
Used to display important recommendation details.
3. head()
Used to display the first few recommendations.
Simple Definition:
Here we are going to give the final summary.
"""
def recommendation_summary(dataset):
    try:
        #Count the total number of products
        total_products = len(dataset)
        print(f"Total Products: {total_products}")
        #Display the first 5 Products
        print("\n Recommendation Summary:")
        print(dataset[["Product_Name","Category","Brand","Sales"]].head())
        return dataset
    except Exception as recommendation_summary_error:
        print("Unable to generate recommendation summary.")
        print(recommendation_summary_error)
        return None