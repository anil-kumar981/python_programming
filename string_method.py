# String are immutable in Python, 
# which means that once a string is created, 
# it cannot be changed. However, 
# you can create new strings based on existing ones using various string methods. 
# Here are some common string methods in Python
# 1. `upper()`: Converts all characters in the string to uppercase.
# 2. `lower()`: Converts all characters in the string to lowercase.
# 3. `capitalize()`: Capitalizes the first character of the string and converts the rest to lowercase.
# 4. `title()`: Capitalizes the first character of each word in the string
# 5. `strip()`: Removes leading and trailing whitespace from the string.
# 6. `replace(old, new)`: Replaces occurrences of a specified substring with another substring.
# 7. `split(separator)`: Splits the string into a list of substrings based on a specified separator.
# 8. `join(iterable)`: Joins elements of an iterable (like a list) into a single string, using the string as a separator.
# 9. `find(substring)`: Returns the lowest index of the substring if it is found in the string, otherwise returns -1.
# 10. `count(substring)`: Returns the number of occurrences of a substring in

string = "Hello, World!"
# Using upper() method
upper_string = string.upper()
print(upper_string)  # Output: "HELLO, WORLD!"

# Using lower() method
lower_string = string.lower()
print(lower_string)  # Output: "hello, world!"

# Using capitalize() method
capitalized_string = string.capitalize()
print(capitalized_string)  # Output: "Hello, world!"

# Using title() method
title_string = string.title()
print(title_string)  # Output: "Hello, World!"

# Using strip() method
whitespace_string = "   Hello, World!   "
stripped_string = whitespace_string.strip()
print(stripped_string)  # Output: "Hello, World!"

# Using replace() method
replaced_string = string.replace("World", "Python")
print(replaced_string)  # Output: "Hello, Python!"

# Using split() method
split_string = string.split(", ")
print(split_string)  # Output: ["Hello", "World!"]

# Using join() method
joined_string = " ".join(split_string)
print(joined_string)  # Output: "Hello World!"

# Using find() method
index = string.find("World")
print(index)  # Output: 7

# Using count() method
count = string.count("o")
print(count)  # Output: 2

