"""
Description:
    Calculates the mode value of a numeric or text column
Concepts used:
1. Mode()
Returns the most frequently occuring value.
Example:
dataset["Price"].mode()
Simple definition:
How many times you go to other class or place for seeing ur girl    
"""
def mode(dataset):
    try:
        mode_value = dataset["Brand"].mode()
        print(f"Mode :\n{mode_value}")
        return dataset
    except Exception as mode_error:
        print("Unable to calculate the mode.")
        print(mode_error)
        return None