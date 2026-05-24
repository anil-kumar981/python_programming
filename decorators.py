# Decorator in python is a design pattern that allows you to modify the behavior of a function or class method without changing its source code.
# A decorator is a function that takes another function as an argument and returns a new function that can add some functionality to the original function.
# Decorators are often used to add functionality to functions or methods, such as logging, timing, or access control.
# Here is an example of a simple decorator that adds logging functionality to a function:

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is called with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs) # This line calls the original function with the provided arguments and keyword arguments, and stores the result in the variable 'result'.
        # in other word above line is calling the original function (the one that is being decorated) with the arguments and keyword arguments that were passed to the wrapper function, 
        # it is storing the return value of the original function in the variable 'result'. It also executes the original function and allows us to capture its output, which we can then log or modify before returning it.
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    print("Inside the add function")
    return a + b

# Example usage
result = add(5, 3)

# Class Decorator
# A class decorator is a function that takes a class as an argument and returns a new class that can add some functionality to the original class.
def class_decorator(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            print(f"Creating an instance of '{cls.__name__}' with arguments: {args} and keyword arguments: {kwargs}")
            self.wrapped_instance = cls(*args, **kwargs)

        def __getattr__(self, name):
            print(f"Accessing attribute '{name}' of the wrapped instance")
            return getattr(self.wrapped_instance, name)

    return Wrapper  

@class_decorator
class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")
    def hello(self):
        print("Hello from MyClass!")

my_instance = MyClass(10)
my_instance.display()  # Output: Value: 10
my_instance.hello()  # Output: Hello from MyClass!