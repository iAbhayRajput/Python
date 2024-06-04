import sys

def display_command_line_arguments():
    # Total number of command-line arguments
    total_arguments = len(sys.argv)

    # Display the total number of arguments
    print("Total number of arguments:", total_arguments)

    # Display each argument
    print("Arguments:")
    for i in range(total_arguments):
        print("Argument " + str(i) + ": " + sys.argv[i])
    
    # Index of the last argument
    last_argument_index = total_arguments - 1
    print("Value of the last argument:", sys.argv[last_argument_index])

def main():
    # Call the function to display command-line arguments
    display_command_line_arguments()

if __name__ == "__main__":
    main()
