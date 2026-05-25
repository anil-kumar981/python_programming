# Super keyword in python is used to call a method from the parent class. It is commonly used in inheritance to access methods and properties of the parent class.
class Parent:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, I am {self.name} from the Parent class."
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calling the __init__ method of the Parent class to initialize the name attribute
        self.age = age
    def greet(self):
        parent_greeting = super().greet()  # Calling the greet method of the Parent class
        return f"{parent_greeting} I am {self.age} years old from the Child class."
# Creating an instance of the Child class
child_instance = Child("Alice", 10)
# Calling the greet method of the Child class, which also calls the greet method of the Parent class using super()
print(child_instance.greet())