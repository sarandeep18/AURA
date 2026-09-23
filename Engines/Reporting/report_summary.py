"""
Description: Displays a summary of the generated report.

Concepts used:

1. shape
   - Returns the number of rows and columns.

2. describe()
   - Provides statistical information about numeric columns.

Real-life Example:
A report summary gives a quick overview
of the processed dataset.
"""


def report_summary(dataset):

    try:

        print("Report Summary")
        print("-------------------------")

        print(f"Total Rows : {dataset.shape[0]}")
        print(f"Total Columns : {dataset.shape[1]}")

        print("\nNumerical Summary:")
        print(dataset.describe())

        return dataset

    except Exception as report_summary_error:

        print("Unable to generate report summary.")
        print(report_summary_error)

        return None