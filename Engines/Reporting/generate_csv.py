"""
Description: Exports the processed dataset into a CSV report.

Concepts used:

1. to_csv()
   - Saves the DataFrame as a CSV file.

2. File Export
   - Used to create a report that can be opened
     outside the AURA application.

Real-life Example:
A CSV report allows the analyzed data to be
shared or opened in spreadsheet software.
"""

def generate_csv(dataset):

    try:

        # Export dataset as CSV
        dataset.to_csv(
            "reports/AURA_report.csv",
            index=False
        )

        print("CSV report generated successfully.")

        return dataset

    except Exception as csv_report_error:

        print("Unable to generate CSV report.")
        print(csv_report_error)

        return None