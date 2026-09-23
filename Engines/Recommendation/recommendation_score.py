"""
Description:
Calculates a simple recommendation score for products based on their sales performance.
Concepts Used:
1. Sorting
Used to arrange products based on their sales.
2. Normalization
Used to convert sales values into a score.
3. DataFrame Operations
Used to create a new recommendation score column.
Simple Definition:
Here AURA is giving products marks.
Higher sales = higher recommendation score.
"""
def recommendation_score(dataset):
    try:
        # Find the highest sales value
        maximum_sales = dataset["Sales"].max()

        # Calculate recommendation score
        dataset["Recommendation_Score"] = (dataset["Sales"] / maximum_sales) * 100

        # Sort products based on recommendation score
        recommendations = dataset.sort_values(by="Recommendation_Score",ascending=False )

        print("Recommendation Scores:")
        print(recommendations[["Product_Name", "Recommendation_Score"]].head())

        return dataset
    except Exception as recommendation_score_error:
        print("Unable to calculate recommendation score.")
        print(recommendation_score_error)
        return None