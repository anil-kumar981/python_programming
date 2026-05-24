# Static method in python
# Static method is a method that belongs to the class rather than an instance of the class. It can be called on the class itself, rather than on an instance of the class.
# Static methods are defined using the @staticmethod decorator, 
# and they do not take the self parameter as the first argument. 
# They can be called using the class name, without creating an instance of the class.

class MyClass:
    @staticmethod
    def static_method():
        return "This is a static method"

# Calling the static method using the class name
print(MyClass.static_method())  # Output: This is a static method

# Static methods can also be called using an instance of the class, 
# but it is not recommended as it can lead to confusion.
my_instance = MyClass()
print(my_instance.static_method())  # Output: This is a static method

# Static methods are often used to create utility functions that are related to the class, 
# but do not require access to instance-specific data.

# The reason we use static methods:
# 1. We don't need to access instance-specific data, so we can define the method as static.
# 2. Static methods can be called without creating an instance of the class, which can be more convenient in some cases.
# 3. And we are not required to pass the self parameter, which can make the code cleaner and easier to read.