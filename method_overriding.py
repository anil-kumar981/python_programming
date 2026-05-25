# Method overriding in python
# Method overriding occurs when a child class provides a specific implementation of a method that is already defined in its parent class. 
# The child class's method overrides the parent class's method when called on an instance of the child class.
class Parent:
    def greet(self):
        return "Hello from the Parent class!"
class Child(Parent):
    def greet(self):
        parent_greeting = super().greet()  # This calls the greet method of the Parent class and stores its return value
        return f"{parent_greeting} Hello from the Child class!"
    
# Creating an instance of the Child class
child_instance = Child()
# Calling the greet method on the child instance will use the overridden method in the Child class
print(child_instance.greet())  # Output: Hello from the Child class!