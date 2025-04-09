def calculator(a, b, operation):
    try:
        if operation.lower() == "add":
            return a + b
        elif operation.lower() == "subtract":
            return a - b
        elif operation.lower() == "multiply":
            return a * b
        elif operation.lower() == "divide":
            if b == 0:
                return "Error: Division by zero is not allowed"
            return a / b
        else:
            return "Error: Operation not supported. Use 'add', 'subtract', 'multiply', or 'divide'"
    except TypeError:
        return "Error: Inputs must be numbers"

if __name__ == "__main__":
    print(calculator(5, 3, "add"))
    print(calculator(5, 3, "subtract"))
    print(calculator(5, 3, "multiply"))
    print(calculator(6, 2, "divide"))
    print(calculator(6, 0, "divide"))
    print(calculator(5, 3, "modulus"))
    print(calculator("5", 3, "add"))
