"""
Description: Exports the processed dataset into an Excel report.

Concepts used:

1. to_excel()
   - Saves the DataFrame as an Excel file.

2. index=False
   - Prevents the DataFrame index from being added
     as an extra column.

Real-life Example:
An Excel report makes the processed data easier
to view and analyze using spreadsheet software.
"""

def generate_excel(dataset):

    try:

        dataset.to_excel(
            "reports/AURA_report.xlsx",
            index=False
        )

        print("Excel report generated successfully.")

        return dataset

    except Exception as excel_report_error:

        print("Unable to generate Excel report.")
        print(excel_report_error)

        return None