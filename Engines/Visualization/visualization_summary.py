"""
Description: Displays a summary of the visualization data.

Concepts used:

1. shape
   - Returns the number of rows and columns.

2. describe()
   - Provides statistical information about numeric columns.

Real-life Example:
A visualization summary gives a quick overview
before creating charts.
"""


def visualization_summary(dataset):

    try:
        # Display dataset dimensions
        print(f"Visualization Rows : {dataset.shape[0]}")
        print(f"Visualization Columns : {dataset.shape[1]}")

        # Display numerical summary
        print("\nVisualization Data Summary:")
        print(dataset.describe())

        return dataset

    except Exception as visualization_summary_error:

        print("Unable to generate visualization summary.")
        print(visualization_summary_error)

        return None