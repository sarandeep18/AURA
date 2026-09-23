"""
Description :
Generates recommendations based on a customer's previous
purchases and the categories they have purchased from.
Concepts Used:
1. Boolean Filtering
Used to find a specific customer's purchase history.
2. unique()
 Used to find the unique categories purchased by the customer.
3. isin()
Used to find products belonging to those categories.
4. DataFrame Filtering
Used to generate the final recommendations.
Simple Definition:
Here we are checking what your customer usually likes.
If they keep buying products from certain categories,
AURA can recommend more products from those categories.
"""
def personalized_recommendation(dataset, customer_id):
    try:
        # Find the customer's purchase history
        customer_data = dataset[dataset["Customer_ID"] == customer_id]
        if customer_data.empty:
            print("Customer not found.")
            return dataset
        # Find categories previously purchased by the customer
        purchased_categories = customer_data["Category"].unique()
        # Find products from those categories
        recommendations = dataset[dataset["Category"].isin(purchased_categories)]
        # Remove products already purchased
        recommendations = recommendations[
            ~recommendations["Product_Name"].isin(customer_data["Product_Name"])]
        print("Personalized Recommendations:")
        print(recommendations)
        return dataset
    except Exception as personalized_recommendation_error:
        print("Unable to generate personalized recommendations.")
        print(personalized_recommendation_error)
        return None