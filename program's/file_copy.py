# Function to copy content from one file to another
def copy_file(source_file, destination_file):
    try:
        # Open source file in read mode
        with open(source_file, 'r') as source:
            # Read content from source file
            content = source.read()
            # Open destination file in write mode
            with open(destination_file, 'w') as destination:
                # Write content to destination file
                destination.write(content)
        print("Content copied successfully from", source_file, "to", destination_file)
        print("\nContent copied from source file:")
        print(content)
    except FileNotFoundError:
        print("File not found.")

# Main function
def main():
    # Take user input for source file and destination file
    source_file = input("Enter the path of the source file: ")
    destination_file = input("Enter the path of the destination file: ")
    
    # Call the function to copy content from source file to destination file
    copy_file(source_file, destination_file)

# Call the main function
if __name__ == "__main__":
    main()
