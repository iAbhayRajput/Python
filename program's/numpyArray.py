#create and manipulate 1-D and 2-D numpy array
import numpy as np

def create_1d_array():
    # Prompt the user to input values for the 1D array
    input_values = input("Enter values for the 1D array (comma-separated): ")
    a = np.array([int(x.strip()) for x in input_values.split(",")])
    
    # Prompt the user to input the desired shape for reshaping the 1D array
    c_shape = tuple(map(int, input("Enter the desired shape for reshaping the 1D array (comma-separated): ").split(",")))
    
    # Reshape the 1D array
    a = a.reshape(c_shape)
    
    return a

def create_2d_array():
    # Prompt the user to input values for the 2D array
    input_values_2d = input("Enter values for the 2D array (comma-separated, rows separated by semicolon): ")
    rows = input_values_2d.split(";")
    b = np.array([[int(x.strip()) for x in row.split(",")] for row in rows])
    return b

def manipulate_arrays(a, b):
    # Print the arrays
    print("1D Array:")
    print(a)
    print("2D Array:")
    print(b)

    # Print the shape and size of the arrays
    print("Shape of the 1D array:", a.shape)
    print("Size of the 1D array:", a.size)
    print("Shape of the 2D array:", b.shape)
    print("Size of the 2D array:", b.size)

    # Print the data type of the arrays
    print("Data type of the 1D array:", a.dtype)
    print("Data type of the 2D array:", b.dtype)

    # Transpose the 2D array
    d = b.T

    # Print the transposed array
    print("Transposed 2D Array:")
    print(d)

    # Flatten the 2D array
    e = b.flatten()

    # Print the flattened array
    print("Flattened 2D Array:")
    print(e)

def main():
    # Create 1D and 2D arrays
    a = create_1d_array()
    b = create_2d_array()

    # Manipulate arrays
    manipulate_arrays(a, b)

if __name__ == "__main__":
    main()
