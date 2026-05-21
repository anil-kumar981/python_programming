# Function in python allow us to reuse a block of code,
# whenever needed. 
# They help in breaking down complex problems into smaller, 
# manageable pieces. Functions can take inputs, perform operations, and return outputs.

# Syntax of a function in python:
# def function_name(parameters):
#     # code block to be executed
#     return value

# Example of a function in python:
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: "Hello, Alice!"

# Another example of a function that takes multiple parameters and returns a value:
def add(a, b):
    return a + b
print(add(5, 3))  # Output: 8

# Functions can also have default parameters, which are used when no argument is provided for that parameter:
def greet(name="World"):
    return f"Hello, {name}!"
print(greet())  # Output: "Hello, World!"
print(greet("Alice"))  # Output: "Hello, Alice!"

# Functions can also return multiple values using tuples:
def get_coordinates():
    x = 10
    y = 20
    return x, y
coordinates = get_coordinates()
print(coordinates)  # Output: (10, 20)

# Functions can also be defined without a return statement, in which case they return None by default:
def print_greeting(name):
    print(f"Hello, {name}!")
result = print_greeting("Alice")  # Output: "Hello, Alice!"
print(result)  # Output: None

# Functions can also be defined with variable-length arguments using *args and **kwargs:
def print_numbers(*args):
    for number in args:
        print(number)
print_numbers(1, 2, 3)  # Output: 1 2 3

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=30)  # Output: name: Alice age: 30

# Functions can also be defined as lambda functions, which are anonymous functions that can take any number of arguments but can only have one expression:
square = lambda x: x * x
print(square(5))  # Output: 25

# Functions can also be defined with both *args and **kwargs to accept variable-length arguments:
def print_value(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_value(1, 2, 3, name="Alice", age=30)
# Output: 1 2 3 name: Alice age: 30
print_value(1)  # Output: 1
print_value(1, name="Alice")  # Output: 1 name: Alice

