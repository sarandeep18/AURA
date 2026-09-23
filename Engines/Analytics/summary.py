"""
Concepts Used
1. dataset.shape
   - Returns the number of rows and columns.
   - Example:
     dataset.shape
     Output: (100, 10)

2. dataset.columns
   - Returns all column names.
   - Example:
     dataset.columns

3. dataset.head()
   - Displays the first 5 rows of the dataset.
   - Useful for checking whether the dataset is loaded correctly.
4. f-Used to insert variables or values inside a string.
"""
def summary(dataset):
    try:
        #display total no of rows
        #counting how many people know your crush
        print(f"Total Rows: {dataset.shape[0]}")
        #display total no of columns
        #Counting how many secrets your crush has
        print(f"Total Columns: {dataset.shape[1]}")
        #Display all column names
        #Checking every follower of your crush
        print(f"\nColumn Names:")
        print(dataset.columns)
        #Display first 5 records
        #First Impression matters
        print(f"\nFirst 5 Records:")
        print(dataset.head())
        return dataset
    except Exception as summary_generation_error:
        print("Unable to generate summary of the dataset.")
        print(summary_generation_error)
        return None