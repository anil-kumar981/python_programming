def welcome(name):
    print(f"Welcome, {name}!")

if __name__ == "__main__":
    welcome("Alice")  # Output: Welcome, Alice!

# Ye isliye hota hai taki jab hum is file ko directly run karein to welcome function execute ho, 
# lekin agar hum is file ko kisi aur file se import karein to welcome function automatically execute na ho.

# More Clear way to understand:
# Jab hum is file ko directly run karte hain, to __name__ variable ki value "__main__" hoti hai, matlab ki ye file main program hai. Isliye welcome("Alice") execute hota hai.
# Lekin jab hum is file ko kisi aur file se import karte hain, to __name__ variable ki value "if_name_main" (ya file ka naam) hoti hai, matlab ki ye file ek module hai. Isliye welcome("Alice") execute nahi hota hai, aur hum apne hisab se welcome function ko call kar sakte hain.
# Aur acche ek example ke sath ye hai jais meri koi file name hai  myfile1.py aur usme __name__ use hua, and hum isi file ko directly run karte hain to __name__ ki value "__main__" hoti hai, 
# aur agar hum is file ko kisi aur file se import karte hain to __name__ ki value "myfile1" hoti hai. Isliye jab hum is file ko directly run karte hain to welcome function execute hota hai, lekin jab hum is file ko kisi aur file se import karte hain to welcome function automatically execute nahi hota hai.
# So iska sidha impact ye hoga 