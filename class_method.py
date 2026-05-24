# Class method decorator
# A class method is a method that belongs to the class rather than an instance of the class. 
# It can be called on the class itself, rather than on an instance of the class.
# Class methods are defined using the @classmethod decorator, and they take the class as the first argument, conventionally named cls.

class MyClass:
    class_variable = "I am a class variable"

    @classmethod
    def class_method(cls, value):
        # cls here refers to the class itself, and we can use it to access class variables and other class methods.
        # The class method can access and modify the class variable using the cls parameter.
        cls.class_variable = value
        return f"This is a class method. Accessing class variable: {cls.class_variable}"

# Calling the class method using the class name
print(MyClass.class_variable)  # Output: This is a class method. Accessing class variable: New value
print(MyClass.class_method("New value"))  # Output: This is a class method.
print(MyClass.class_variable)  # Output: New value


# Using Class method to create an alternative constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, person_string):
        name, age = person_string.split(",")
        return cls(name, int(age)) # This calls the original constructor of the class (the __init__ method) with the name and age extracted from the string, and returns an instance of the Person class. This allows us to create a Person object from a string representation, providing an alternative way to instantiate the class.

# Creating an instance of Person using the alternative constructor
person = Person.from_string("Alice,30")
print(person.name)  # Output: Alice
print(person.age)   # Output: 30