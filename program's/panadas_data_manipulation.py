import pandas as pd

def create_series():
    # Prompt the user to input values for the Series
    input_values = input("Enter values for the Series (space-separated): ")
    values = [int(x.strip()) for x in input_values.split()]
    
    # Prompt the user to input index labels for the Series
    index_labels = input("Enter index labels for the Series (space-separated): ").split()

    
    # Create the Series
    series = pd.Series(values, index=index_labels)
    return series


def manipulate_series(series):
    print("\nOriginal Series:")
    print(series)
    
    # Accessing elements of the Series
    print("\nAccessing elements of the Series:")
    index_label = input("Enter an index label to access the element: ")
    print("Element at index '{}':".format(index_label), series[index_label])
    
    # Performing arithmetic operations on Series
    print("\nArithmetic operations on Series:")
    scalar_value = int(input("Enter a scalar value for arithmetic operations: "))
    print("Series multiplied by {}: ".format(scalar_value))
    print(series * scalar_value)
    
def create_dataframe():
    # Prompt the user to input data for the DataFrame
    data = {}
    for col in ['Name', 'Age', 'City']:
        values = input("Enter values for column '{}': ".format(col)).split(",")
        data[col] = values
    
    # Create the DataFrame
    df = pd.DataFrame(data)
    return df

def manipulate_dataframe(df):
    print("\nOriginal DataFrame:")
    print(df)
    
    # Accessing columns of the DataFrame
    print("\nAccessing columns of the DataFrame:")
    col_name = input("Enter a column name to access the column: ")
    print("Column '{}':".format(col_name))
    print(df[col_name])
    
    # Adding a new column to the DataFrame
    new_col_name = input("Enter a name for the new column: ")
    new_col_values = input("Enter values for the new column (comma-separated): ").split(",")
    df[new_col_name] = new_col_values
    print("\nDataFrame after adding column '{}':".format(new_col_name))
    print(df)
    
    # Removing a column from the DataFrame
    remove_col_name = input("Enter the name of the column to remove: ")
    df.drop(columns=[remove_col_name], inplace=True)
    print("\nDataFrame after removing column '{}':".format(remove_col_name))
    print(df)
    
    # Applying a function to a column
    apply_col_name = input("Enter the name of the column to apply function: ")
    df[apply_col_name] = df[apply_col_name].apply(lambda x: int(x) + 1)
    print("\nDataFrame after applying function to column '{}':".format(apply_col_name))
    print(df)

def main():
    print("Options:")
    print("1. Create and manipulate Series")
    print("2. Create and manipulate DataFrame")
    choice = int(input("Enter your choice (1 or 2): "))
    
    if choice == 1:
        # Create and manipulate Series
        series = create_series()
        manipulate_series(series)
    elif choice == 2:
        # Create and manipulate DataFrame
        df = create_dataframe()
        manipulate_dataframe(df)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
