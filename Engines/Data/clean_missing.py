"""
Description:
In this file, we clean the missing values in the dataset.

Example of missing values in the dataset:

| Product | Brand  | Price |
|---------|--------|------:|
| Shirt   | Nike   |  1200  |
| Shoes   | Empty  |  2500  |
| Jeans   | Levi's |  1800  |
"""

import pandas as pd


def clean_missing_values(dataset):

    try:

        # Counting the number of missing values
        missing_values_count = dataset.isnull().sum().sum()

        # Checking if there are any missing values
        if missing_values_count == 0:

            print("AURA Data Check Passed")
            print("No missing values found in the dataset.")

            return dataset

        else:

            print("AURA Data Check Warning")
            print(f"Total missing values : {missing_values_count}")

            # Counting rows before cleaning
            rows_before = dataset.shape[0]

            # Removing rows containing missing values
            cleaned_dataset = dataset.dropna()

            # Counting rows after cleaning
            rows_after = cleaned_dataset.shape[0]

            # Displaying the number of removed rows
            print(f"Rows Removed : {rows_before - rows_after}")
            print("Dataset cleaned successfully.")

        return cleaned_dataset

    except Exception as cleaning_error:

        print("Unable to clean missing values from the dataset.")
        print(cleaning_error)

        return None