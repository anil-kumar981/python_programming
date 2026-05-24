# Getter and Setter in Python
# In Python, we can use the @property decorator to create getter and setter methods for class attributes.
# The @property decorator allows us to define a method that can be accessed like an attribute, and the @<attribute>.setter decorator allows us to define a method that can be used to set the value of that attribute.

class MyClass:
    def __init__(self, value):
        self._value = value  # Using a single underscore to indicate that this attribute is intended to be private

    @property
    def value(self):
        """The getter method for the 'value' property."""
        print("Getting the value")
        return self._value

    @value.setter
    def value(self, new_value):
        """The setter method for the 'value' property."""
        print("Setting the value")
        self._value = new_value

my_instance = MyClass(10)
print(my_instance.value)  
my_instance.value = 20
print(my_instance.value)