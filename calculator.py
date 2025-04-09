from addition import add_integers
from subtraction import subtract_integers  # If available
from multiplication import multiply_integers
from division import divide_integers

def calculator(a, b, operation):
    if operation == "add":
        return add_integers(a, b)
    elif operation == "subtract":
        return subtract_integers(a, b)
    elif operation == "multiply":
        return multiply_integers(a, b)
    elif operation == "divide":
        return divide_integers(a, b)
    else:
        return "Operation not supported"

# Test
if _name_ == "_main_":
    print(calculator(5, 3, "add"))        # Prints 8
    print(calculator(5, 3, "subtract"))   # Prints 2 (if subtract exists)
    print(calculator(5, 3, "multiply"))   # Prints 15
    print(calculator(6, 2, "divide"))     # Prints 3