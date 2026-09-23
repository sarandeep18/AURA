"""
Description: Creates a line chart to display sales progression.

Concepts used:

1. plot()
   - Creates a line chart.

2. sort_values()
   - Sorts the data before plotting.

Real-life Example:
A line chart helps observe how sales change over time.
"""

import matplotlib.pyplot as plt


def line_chart(dataset):

    try:
        # Sort data by order date
        chart_data = dataset.sort_values("Order_Date")

        plt.plot(chart_data["Order_Date"], chart_data["Sales"])

        plt.title("Sales Trend")
        plt.xlabel("Order Date")
        plt.ylabel("Sales")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        return dataset

    except Exception as line_chart_error:

        print("Unable to create line chart.")
        print(line_chart_error)

        return None