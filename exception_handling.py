# Exception handling in Python

# Exception handling is a mechanism in Python to handle errors gracefully without crashing the program.
# In Python, we use the try-except block to handle exceptions. The code that may raise an exception is placed inside the try block, and the code to handle the exception is placed inside the except block.
# Example of exception handling in Python:
try:
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Output: Error: division by zero

# With functions:
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return f"Error: {e}"
print(divide(10, 0))  # Output: Error: division by zero

# Many types of exceptions can be handled in Python
# Divide by zero error
# ZeroDivisionError: division by zero
# File not found error
# FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'
# Value error
# ValueError: invalid literal for int() with base 10: 'abc'
# Type error
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Index error
# IndexError: list index out of range
# Key error
# KeyError: 'key'
# You can also handle multiple exceptions in a single except block:
try:
    x = 10 / 0
except (ZeroDivisionError, ValueError) as e:
    print(f"Error: {e}")  # Output: Error: division by zero

# You can also use the else block to execute code if no exceptions were raised:
try:
    x = 10 / 2
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print(f"Result: {x}")  # Output: Result: 5.0