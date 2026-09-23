"""
Description: Creates a box plot to analyze the distribution
of product prices and identify possible outliers.

Concepts used:

1. boxplot()
   - Creates a box plot.

2. DataFrame columns
   - Used to select the numeric column.

Real-life Example:
A box plot helps identify the middle range of data
and possible unusual values.
"""

import matplotlib.pyplot as plt


def box_plot(dataset):

    try:
        # Creating the box plot
        plt.boxplot(dataset["Price"])

        plt.title("Price Distribution")
        plt.ylabel("Price")
        plt.tight_layout()
        plt.show()

        return dataset

    except Exception as box_plot_error:

        print("Unable to create box plot.")
        print(box_plot_error)

        return None