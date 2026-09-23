"""
Description: Creates a scatter plot showing the relationship
between Price and Sales.

Concepts used:

1. scatter()
   - Creates a scatter plot.

2. DataFrame columns
   - Used to select numeric columns.

Real-life Example:
A scatter plot helps identify whether two values
have a relationship.
"""

import matplotlib.pyplot as plt


def scatter_plot(dataset):

    try:
        # Creating the scatter plot
        plt.scatter(dataset["Price"], dataset["Sales"])

        plt.title("Price vs Sales")
        plt.xlabel("Price")
        plt.ylabel("Sales")
        plt.tight_layout()
        plt.show()

        return dataset

    except Exception as scatter_plot_error:

        print("Unable to create scatter plot.")
        print(scatter_plot_error)

        return None