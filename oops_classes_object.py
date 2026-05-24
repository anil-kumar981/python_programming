# Note: Ye code ek simple class definition hai, 
# jisme ek student class banaya gaya hai. 
# Is class ke andar ek

# In python hame variable ko define karne ke liye __init__ method ka use karte hain, ye dyanmically variable ko create karta hai,
# aur jab bhi hum student class ka object banayenge to __init__ method automatically call hoga, 
# aur usme hum name aur age variable ko initialize karenge.
# and jab ham object banate hain to hame class ke constructor ko jine varaible define hai unhe pass karna hota hai, jese ki name aur age variable ko pass karna hoga.
class Student:
    def __init__(self, n, a):
            self.name = n
            self.age = a

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# s = Student() # Now this will give an error because we are not passing the required arguments (name and age) to the constructor.
s = Student("Alice", 20) # This will work because we are passing the required arguments (name and age) to the constructor.
s.display_info()