def perform_operation(op, num1, num2):
    if op == 1:
        return num1 + num2
    elif op == 2:
        return num1 - num2
    elif op == 3:
        return num1 * num2
    elif op == 4:
        return num1 / num2
    elif op == 5:
        return num1 % num2
    elif op == 6:
        return num1 ** num2
    else:
        return "Invalid operation"

print("Here are the numbers for required operations:")
print("Addition: '1'")
print("Subtraction: '2'")
print("Multiplication: '3'")
print("Division: '4'")
print("Modulus: '5'")
print("Exponentiation: '6'")

operation = int(input("Enter the number for the required operation: "))
input_1 = float(input("Enter the first number: "))
input_2 = float(input("Enter the second number: "))

result = perform_operation(operation, input_1, input_2)
print("Result:", result)
