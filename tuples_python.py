# Tuples in Python
# A tuple is an ordered, immutable collection of items.
# Tuples are defined by enclosing the items in parentheses () and separating them with commas.  
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4

# Tuples can contain items of different types, including other tuples:
mixed_tuple = (1, "Hello", 3.14, (1, 2, 3))
print(mixed_tuple)  # Output: (1, "Hello", 3.14, (1, 2, 3))

# Tuples are immutable, which means you cannot change their content after they have been created:
# The following line will raise a TypeError:
# my_tuple[0] = 10
# You can access items in a tuple using their index:
print(my_tuple[0])  # Output: 1

# You can also use negative indexing to access items from the end of the tuple:
print(my_tuple[-1])  # Output: 5
# Tuples also support slicing, which allows you to access a range of items:
print(my_tuple[1:4])  # Output: (2, 3, 4)
print(my_tuple[:3])  # Output: (1, 2, 3)
print(my_tuple[3:])  # Output: (4, 5)

# You can also use the len() function to get the number of items in a tuple:
print(len(my_tuple))  # Output: 5

# Tuples can also be nested, which means you can have tuples within tuples:
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple)  # Output: (1, 2, (3, 4), 5)
print(nested_tuple[2])  # Output: (3, 4)
print(nested_tuple[2][0])  # Output: 3

# Tuples also support various methods for manipulating their content, such as count() and index():
print(my_tuple.count(2))  # Output: 1
print(my_tuple.index(3))  # Output: 2

# You can also use tuple unpacking to assign values from a tuple to variables:
a, b, c, d, e = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(d)  # Output: 4
print(e)  # Output: 5

# You can also use the * operator to unpack a tuple into a list:
my_list = [*my_tuple] # ( asterisk operator is used to unpack the tuple into a list)
print(my_list)  # Output: [1, 2, 3, 4, 5]

