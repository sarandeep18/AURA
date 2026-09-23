"""
Project : AURA
Version : 1.0

Description :
Removes duplicate values from the dataset.

Example of duplicate values:

| Product | Brand | Price |
|---------|-------|------:|
| Shirt   | Nike  |  1200 |
| Shoes   | Puma  |  2500 |
| Shirt   | Nike  |  1200 |
"""

import pandas as pd


def remove_duplicates(dataset):

    try:

        # Counting the number of duplicate values
        duplicate_values_count = dataset.duplicated().sum()

        # Checking if there are any duplicate values
        if duplicate_values_count == 0:

            print("No duplicate values found in the dataset.")

            return dataset

        else:

            print(
                f"Total duplicate values : {duplicate_values_count}"
            )

            # Counting rows before removing duplicates
            rows_before = dataset.shape[0]

            # Removing duplicate values from the dataset
            cleaned_dataset = dataset.drop_duplicates()

            # Counting rows after removing duplicates
            rows_after = cleaned_dataset.shape[0]

            # Displaying the number of removed rows
            print(f"Rows Removed : {rows_before - rows_after}")
            print("Duplicate values removed successfully.")

            return cleaned_dataset

    except Exception as duplicate_error:

        print("Unable to remove duplicate values from the dataset.")
        print(duplicate_error)

        return None