"""
Description: Creates a bar chart using categorical data from the dataset.

Concepts used:

1. bar()
   - Creates a bar chart.

2. DataFrame columns
   - Used to select the required columns.

Real-life Example:
A bar chart helps compare different categories,
just like comparing sales of different products.
"""

import matplotlib.pyplot as plt


def bar_chart(dataset):

    try:
        # Creating the bar chart
        dataset.groupby("Product_Name")["Sales"].sum().plot(kind="bar")

        plt.title("Product Sales")
        plt.xlabel("Product")
        plt.ylabel("Sales")
        plt.tight_layout()
        plt.show()

        return dataset

    except Exception as bar_chart_error:

        print("Unable to create bar chart.")
        print(bar_chart_error)

        return None