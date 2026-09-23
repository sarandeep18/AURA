"""
Description:
Provides recommendations based on products previously purchased by a customer.
Concepts Used:
1.Boolean Filtering
Used to find records belonging to a particular customer.
2.Unique()
Returns unique values from a column.
3. DataFrame Filtering
Used to retrieve products purchased by the customer.
Simple Definition:
Here we are checking what your customer already bought.
Because if the customer already owns the product,
recommending the exact same thing again is not very helpful.
"""
def collaborative_filtering(dataset, customer_id):
    try:
        #Finds purchases made by the selected customer
        customer_data = dataset[dataset["Customer_ID"] == customer_id]
        if customer_data.empty:
            print("Customer not found.")
            return dataset
        #Get products already purchased by the customer
        purchased_products = customer_data["Product_Name"].unique()
        print("Previously Purchased Products:")
        #Find products that the customer has not purchased
        recommendations = dataset[~dataset["Product_Name"].isin(purchased_products)]
        print("\nRecommended Products:")
        print(recommendations)
        return dataset
    except Exception as recommendation_error:
        print("Unable to generate collabrative recommendations.")
        print(recommendation_error)
        return None