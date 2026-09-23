"""
Description: Creates a heatmap showing correlations between
numeric columns in the dataset.

Concepts used:

1. corr()
   - Calculates correlation between numeric columns.

2. heatmap()
   - Displays correlation values visually.

Real-life Example:
A heatmap makes relationships between multiple
numeric columns easier to understand.
"""

import matplotlib.pyplot as plt
import seaborn as sns


def heatmap(dataset):

    try:
        # Select numeric columns
        numeric_data = dataset.select_dtypes(include="number")

        # Calculate correlation
        correlation_matrix = numeric_data.corr()

        # Create heatmap
        sns.heatmap(
            correlation_matrix,
            annot=True
        )

        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.show()

        return dataset

    except Exception as heatmap_error:

        print("Unable to create heatmap.")
        print(heatmap_error)

        return None