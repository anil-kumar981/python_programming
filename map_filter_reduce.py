# syntax : map(function, iterable)
# map function is used to apply a given function to all items in an iterable (like list, tuple, etc.) and returns a map object (which is an iterator).
# Example 1: Using map to square each number in a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]
# Example 2: Using map to convert a list of strings to uppercase
strings = ["hello", "world", "python"]
uppercase_strings = map(lambda s: s.upper(), strings)
print(list(uppercase_strings))  # Output: ['HELLO', 'WORLD', 'PYTHON']

# Now without using lambda function
def square(x):
    return x**2
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# syntax : filter(function, iterable)
# filter function is used to filter items in an iterable based on a given function that returns True or False. It returns a filter object (which is an iterator).
# Example 1: Using filter to get even numbers from a list
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]

# Without using lambda function
def is_even(x):
    return x % 2 == 0
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # Output: [2, 4]

# syntax : reduce(function, iterable)
# reduce function is used to apply a given function cumulatively to the items of an iterable, 
# from left to right, so as to reduce the iterable to a single value. 
# It is part of the functools module in Python.
from functools import reduce
# Example 1: Using reduce to calculate the product of all numbers in a list 
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# Without using lambda function
def multiply(x, y):
    return x * y
product = reduce(multiply, numbers)
print(product)  # Output: 120