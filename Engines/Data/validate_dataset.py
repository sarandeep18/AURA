"""
Project : AURA
Version : 1.0

Description :
Checks whether the dataset is valid or not.
"""


def validate_dataset(dataset):

    try:

        # Checking whether the dataset was loaded successfully
        if dataset is None:

            print("Dataset validation failed.")
            return False

        print("Dataset is valid.")
        return True

    except Exception as validation_error:

        print("Unable to validate the dataset.")
        print(validation_error)

        return False