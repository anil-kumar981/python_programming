# Rasie in Python
# In Python, you can raise an exception using the raise statement.
# The raise statement allows you to create and throw an exception, which can be caught and handled
# by the calling code. You can raise built-in exceptions or create your own custom exceptions.

# Example of raising a built-in exception:
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")  # Output: Error: Cannot divide by zero