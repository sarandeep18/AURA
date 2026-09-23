"""
Description: Generates a PDF report containing the dataset summary.

Concepts used:

1. reportlab
   - Used to create PDF documents.

2. SimpleDocTemplate
   - Used to create the PDF document.

3. Paragraph
   - Used to add text to the PDF.

Real-life Example:
A PDF report provides a portable format
for sharing the project results.
"""

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(dataset):

    try:

        pdf_path = "reports/AURA_report.pdf"

        document = SimpleDocTemplate(
            pdf_path,
            pagesize=letter
        )

        styles = getSampleStyleSheet()

        report_content = []

        report_content.append(
            Paragraph(
                "AURA Data Report",
                styles["Title"]
            )
        )

        report_content.append(
            Paragraph(
                f"Total Rows: {dataset.shape[0]}",
                styles["Normal"]
            )
        )

        report_content.append(
            Paragraph(
                f"Total Columns: {dataset.shape[1]}",
                styles["Normal"]
            )
        )

        document.build(report_content)

        print("PDF report generated successfully.")

        return dataset

    except Exception as pdf_report_error:

        print("Unable to generate PDF report.")
        print(pdf_report_error)

        return None