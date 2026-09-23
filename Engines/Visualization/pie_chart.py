"""
Description: Creates a pie chart showing sales distribution by category.

Concepts used:

1. groupby()
   - Groups data according to category.

2. pie()
   - Creates a pie chart.

Real-life Example:
A pie chart shows how the total sales are divided
among different product categories.
"""

import matplotlib.pyplot as plt


def pie_chart(dataset):

    try:
        # Calculate sales by category
        category_sales = dataset.groupby("Category")["Sales"].sum()

        plt.pie(
            category_sales,
            labels=category_sales.index,
            autopct="%1.1f%%"
        )

        plt.title("Sales Distribution by Category")
        plt.show()

        return dataset

    except Exception as pie_chart_error:

        print("Unable to create pie chart.")
        print(pie_chart_error)

        return None