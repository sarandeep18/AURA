"""
Project : AURA
Version : 1.0
Description :
Loads a CSV dataset into a Pandas DataFrame.
"""
#import pandas module
import pandas as pd
def load_dataset():
        try:
            dataset = pd.read_csv("Dataset/RAW/AURA.csv")#Idiot read the file
            print("AURA files engaged successfully! AURA+++")#User found
            #using shape attribute to get number of rows and columns
            print(f"Rows : {dataset.shape[0]}")#printing number of rows
            print(f"Columns : {dataset.shape[1]}")#printing number of columns
            return dataset
        except FileNotFoundError as dataset_is_not_found:
            print("dataset not found")
            return None