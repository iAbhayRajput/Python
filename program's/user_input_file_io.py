# Function to write user input to a file
def write_to_file(user_input, filename):
    try:
        # Open the file in write mode ('w')
        with open(filename, 'w') as file:
            # Write user input to the file
            file.write(user_input + '\n')
        print("Text has been written to the file successfully.")
    except FileNotFoundError:
        print("File not found.")

# Function to read content from a file
def read_from_file(filename):
    try:
        # Open the file in read mode ('r')
        with open(filename, 'r') as file:
            # Read the entire file content
            content = file.read()
            print("\nContent of the file in read mode:")
            print(content)
    except FileNotFoundError:
        print("File not found.")

# Main function
def main():
    # Take user input for the filename
    filename = input("Enter the filename: ")
    
    # Take user input for the text to be written to the file
    user_input = input("Enter the text to write to the file: ")

    
    # Write user input to the file
    write_to_file(user_input, filename)
    
    # Read content from the file
    read_from_file(filename)

# Call the main function
if __name__ == "__main__":
    main()
