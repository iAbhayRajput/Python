import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_dataset():
    file_path = input("Enter the path to your dataset file: ")
    df = pd.read_csv(file_path)
    return df

def generate_histogram(df):
    column_name = input("Enter the name of the column for histogram: ")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x=column_name, bins=20, kde=True)
    plt.title('Histogram of {}'.format(column_name))
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.show()

def generate_scatterplot(df):
    column1 = input("Enter the name of the x-axis column for scatterplot: ")
    column2 = input("Enter the name of the y-axis column for scatterplot: ")
    category_column = input("Enter the name of the category column for coloring (optional): ")
    plt.figure(figsize=(10, 6))
    if category_column:
        sns.scatterplot(data=df, x=column1, y=column2, hue=category_column, palette='viridis')
        plt.legend(title=category_column)
    else:
        sns.scatterplot(data=df, x=column1, y=column2)
    plt.title('Scatterplot of {} vs {}'.format(column1, column2))
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.show()

def main():
    df = load_dataset()
    print("\nDataset loaded successfully.")
    
    while True:
        print("\nOptions:")
        print("1. Generate Histogram")
        print("2. Generate Scatterplot")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            generate_histogram(df)
        elif choice == '2':
            generate_scatterplot(df)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
