# List in Python
# A list is a collection of items that are ordered and changeable.
# Lists are defined by enclosing the items in square brackets [] and separating them with commas.
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Lists can contain items of different types, including other lists:
mixed_list = [1, "Hello", 3.14, [1, 2, 3]]
print(mixed_list)  # Output: [1, "Hello", 3.14, [1, 2, 3]]

# Lists are mutable, which means you can change their content after they have been created:
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]

# You can also add items to a list using the append() method:
my_list.append(6)
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]

# You can remove items from a list using the remove() method:
my_list.remove(2)
print(my_list)  # Output: [10, 3, 4, 5, 6]

# You can also use the pop() method to remove an item at a specific index:
popped_item = my_list.pop(1)
print(popped_item)  # Output: 3
print(my_list)  # Output: [10, 4, 5, 6]

# You can access items in a list using their index:
print(my_list[0])  # Output: 10
print(my_list[1])  # Output: 4

# You can also use negative indexing to access items from the end of the list:
print(my_list[-1])  # Output: 6
print(my_list[-2])  # Output: 5

# Lists also support slicing, which allows you to access a range of items:
print(my_list[1:3])  # Output: [4, 5]
print(my_list[:2])  # Output: [10, 4]
print(my_list[2:])  # Output: [5, 6]    

# You can also use the len() function to get the number of items in a list:
print(len(my_list))  # Output: 4

# Lists can also be nested, which means you can have lists within lists:
nested_list = [1, 2, [3, 4], 5]
print(nested_list)  # Output: [1, 2, [3, 4], 5]
print(nested_list[2])  # Output: [3, 4]
print(nested_list[2][0])  # Output: 3

# Lists also support various methods for manipulating their content, such as sort(), reverse(), and extend():
my_list.sort()
print(my_list)  # Output: [4, 5, 6, 10]
my_list.reverse()
print(my_list)  # Output: [10, 6, 5, 4
my_list.extend([7, 8, 9])
print(my_list)  # Output: [10, 6, 5, 4, 7, 8, 9]

# You can also use list comprehensions to create new lists based on existing ones:
squared_list = [x**2 for x in my_list]
print(squared_list)  # Output: [100, 36, 25, 16, 49, 64, 81]

# Lists are a powerful and versatile data structure in Python that can be used to store and manipulate collections of items.
