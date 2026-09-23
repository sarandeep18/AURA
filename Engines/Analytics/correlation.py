"""
Description:
Calculates the correlation between numeric columns in the dataset.
Concepts used:
corr():
Returns the correlation between numeric columns.
Example:
dataset.corr(numeric_only=True)
Simple Definition:
Just like checking whether two best friends
always move together, correlation tells us
how two columns are related.
"""
def correlation(dataset):

    try:

        # Select numeric columns
        numeric_data = dataset.select_dtypes(include="number")

        # Calculate correlation between numeric columns
        correlation_matrix = numeric_data.corr()

        print("Correlation Matrix:")
        print(correlation_matrix)

        return dataset

    except Exception as correlation_error:

        print("Correlation not found")
        print(correlation_error)

        return None