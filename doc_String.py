# DocString in Python
# A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition.
# It is used to document the purpose and behavior of the code it describes.
# Docstrings are enclosed in triple quotes (""" """) and can span multiple lines.
# They are accessible through the __doc__ attribute of the object they document.
# Here is an example of a function with a docstring:
def greet(name):
    """This function takes a name as an argument 
    and returns a greeting message."""
    return f"Hello, {name}!"
print(greet("Alice"))  # Output: "Hello, Alice!"
print(greet.__doc__)  # Output: "This function takes a name as an argument and returns a greeting message."

# It is written immediately after the function definition and provides a description of what the function does, its parameters, and its return value.
# example of a class with a docstring:
class Person:
    """This class represents a person with a name and age."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        """This method returns a greeting message."""
        return f"Hello, my name is {self.name} and I am {self.age} years old."
person = Person("Alice", 30)
print(person.greet())  # Output: "Hello, my name is Alice and I am 30 years old."
print(Person.__doc__)  # Output: "This class represents a person with a name and age."
print(Person.greet.__doc__)  # Output: "This method returns a greeting message."