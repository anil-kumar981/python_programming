# Access Modifiers in Python
# In Python, there are three types of access modifiers: public, protected, and private.
# 1. Public Access Modifier:
#    - Public members (attributes and methods) can be accessed from anywhere, both inside and
#      outside the class. They are defined without any special prefix.
# 2. Protected Access Modifier:
#    - Protected members are intended to be accessed only within the class and its subclasses. They are defined with a single underscore prefix (_).
# 3. Private Access Modifier:
#    - Private members are intended to be accessed only within the class. They are defined with a double underscore prefix (__).
# Example of access modifiers in Python:
class MyClass:
    def __init__(self):
        self.public_attribute = "I am public"
        self._protected_attribute = "I am protected" # Single underscore indicates that this attribute is intended to be protected, meaning it should not be accessed directly from outside the class or its subclasses.
        self.__private_attribute = "I am private" # Double underscore indicates that this attribute is intended to be private, meaning it should not be accessed directly from outside the class.
    def public_method(self):
        return "This is a public method"
    def _protected_method(self):
        return "This is a protected method"
    def __private_method(self):
        return "This is a private method"
my_instance = MyClass()
# Accessing public members  
print(my_instance.public_attribute)  # Output: I am public
print(my_instance.public_method())  # Output: This is a public method
# Accessing protected members (not recommended, but possible)
print(my_instance._protected_attribute)  # Output: I am protected
print(my_instance._protected_method())  # Output: This is a protected method
# Accessing private members (not recommended, but possible using name mangling)
print(my_instance._MyClass__private_attribute)  # Output: I am private
print(my_instance._MyClass__private_method())  # Output: This is a private method