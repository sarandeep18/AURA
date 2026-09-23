"""
Description: Creates a histogram showing the distribution of prices.

Concepts used:

1. hist()
   - Creates a histogram.

2. DataFrame columns
   - Used to select the numeric column.

Real-life Example:
A histogram helps understand how values are distributed
across different ranges.
"""

import matplotlib.pyplot as plt


def histogram(dataset):

    try:
        # Creating the histogram
        plt.hist(dataset["Price"], bins=10)

        plt.title("Price Distribution")
        plt.xlabel("Price")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()

        return dataset

    except Exception as histogram_error:

        print("Unable to create histogram.")
        print(histogram_error)

        return None