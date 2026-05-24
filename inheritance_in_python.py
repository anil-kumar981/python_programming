# Inheritance in python
# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (called a child or subclass) to inherit properties and behaviors (attributes and methods) from an existing class (called a parent or superclass).
# The main advantage of inheritance is that it promotes code reusability and establishes a natural hierarchical relationship between classes.
# In Python, you can create a child class that inherits from a parent class using the following syntax:
# Syntax:
# class ParentClass:
#     # parent class code
# class ChildClass(ParentClass):
#     # child class code
# Example of inheritance in Python:
# Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.name)  # Output: Buddy
print(dog.speak())  # Output: Woof!
print(cat.name)  # Output: Whiskers
print(cat.speak())  # Output: Meow!

# Multiple Inheritance
# In multiple inheritance, a child class can inherit from more than one parent class. This allows the child class to have access to the attributes and methods of all the parent classes.
class Flyer:
    def fly(self):
        return "Flying"
class Swimmer:
    def swim(self):
        return "Swimming"
class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack!"
duck = Duck()
print(duck.fly())  # Output: Flying
print(duck.swim())  # Output: Swimming
print(duck.quack())  # Output: Quack!

# Multilevel Inheritance
# In multilevel inheritance, a child class inherits from a parent class, and then another child class inherits from that child class, creating a chain of inheritance.
class Vehicle:
    def move(self):
        return "Moving"
class Car(Vehicle):
    def drive(self):
        return "Driving"
class SportsCar(Car):
    def turbo(self):
        return "Turbo mode"
sports_car = SportsCar()
print(sports_car.move())  # Output: Moving
print(sports_car.drive())  # Output: Driving
print(sports_car.turbo())  # Output: Turbo mode

# Hierarchical Inheritance
# In hierarchical inheritance, multiple child classes inherit from a single parent class.
class Shape:
    def area(self):
        return "Area of shape"
class Circle(Shape):
    def area(self):
        return "Area of circle"
class Square(Shape):
    def area(self):
        return "Area of square"
circle = Circle()
square = Square()
print(circle.area())  # Output: Area of circle
print(square.area())  # Output: Area of square

# Hybrid Inheritance
# Hybrid inheritance is a combination of two or more types of inheritance. It allows for more complex relationships between classes.
class A:
    def method_a(self):
        return "Method A"
class B(A):
    def method_b(self):
        return "Method B"
class C(A):
    def method_c(self):
        return "Method C"
class D(B, C):
    def method_d(self):
        return "Method D"
d = D()
print(d.method_a())  # Output: Method A 
print(d.method_b())  # Output: Method B
print(d.method_c())  # Output: Method C
print(d.method_d())  # Output: Method D

