"""
Description: Manages the generation of all AURA reports.

Concepts used:

1. Function Calls
   - Used to execute different reporting functions.

2. Modular Programming
   - Combines multiple reporting modules
     into a single reporting process.

Real-life Example:
Instead of manually generating every report,
the report manager handles the complete process.
"""

from Engines.Reporting.generate_csv import generate_csv
from Engines.Reporting.generate_excel import generate_excel
from Engines.Reporting.generate_pdf import generate_pdf
from Engines.Reporting.report_summary import report_summary
from Engines.Reporting.export_logs import export_logs


def report_manager(dataset):

    try:

        dataset = report_summary(dataset)

        dataset = generate_csv(dataset)

        dataset = generate_excel(dataset)

        dataset = generate_pdf(dataset)

        dataset = export_logs(dataset)

        print("All AURA reports generated successfully.")

        return dataset

    except Exception as report_manager_error:

        print("Unable to complete report generation.")
        print(report_manager_error)

        return None