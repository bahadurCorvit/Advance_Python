# ===========================================================
# Python Practice - Printing, Input, String Manipulation
# From Beginner to Professional Level
# ===========================================================

# -------------------- 1. Printing Constants and Variables --------------------
print("=== Printing Constants ===")
print("Hello, Python!")    # String constant
print(42)                   # Integer constant
print(3.14)                  # Float constant
print(True)                  # Boolean constant
print("-" * 50)

# Variables
print("=== Printing Variables ===")
name = "Fawad"
age = 22
cgpa = 3.75

print(name)
print(age)
print(cgpa)
print("Name:", name, "Age:", age, "CGPA:", cgpa)
print("-" * 50)

# Exercise 1
color = "Blue"
height = 5.9
my_age = 21
print("My favorite color is", color, "I am", my_age, "years old and my height is", height, "ft")
print("-" * 50)

# -------------------- 2. F-Strings for Formatting --------------------
language = "Python"
version = 3.10
print(f"I am learning {language} version {version}.")
print("-" * 50)

# Exercise 2
city = "Karachi"
country = "Pakistan"
population = 20_000_000
print(f"My city is {city} in {country} with a population of {population}.")
print("-" * 50)

# -------------------- 3. Accepting User Input --------------------
print("=== User Input ===")
# Simple input
# Uncomment to test
# user_name = input("Enter your name: ")
# user_age = input("Enter your age: ")
# print("Hello,", user_name, "! You are", user_age, "years old.")

# Numeric input with type conversion
# Uncomment to test
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print("Sum:", num1 + num2)

print("-" * 50)

# Exercise 3
# Uncomment to test
# movie = input("Enter your favorite movie: ")
# rating = input("Rate it (1-10): ")
# print(f"You rated {movie} {rating} out of 10.")
print("-" * 50)

# -------------------- 4. String Concatenation --------------------
first_name = "Fawad"
last_name = "Bahadur"
full_name = first_name + " " + last_name
print("Full Name:", full_name)
print("-" * 50)

# User input concatenation
# Uncomment to test
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# print("Hello,", first_name + " " + last_name)
print("-" * 50)

# Exercise 4
city = "Karachi"
country = "Pakistan"
print(city + " is in " + country + ".")
print("-" * 50)

# -------------------- 5. String Manipulation Basics --------------------
message = "  Python Programming  "
print("Original:", repr(message))
print("Strip:", message.strip())          # Remove spaces both sides
print("Uppercase:", message.upper())      # Convert to uppercase
print("Lowercase:", message.lower())      # Convert to lowercase
print("Count of 'o':", message.count('o'))  # Count character
print("Replace 'Python' with 'Java':", message.replace("Python", "Java"))
print("-" * 50)

# Exercise 5
sentence = "  Hello World from Python  "
print("Characters count:", len(sentence))
print("Uppercase:", sentence.upper())
print("Stripped:", sentence.strip())
print("Spaces replaced with underscore:", sentence.strip().replace(" ", "_"))
print("-" * 50)

# -------------------- 6. Combining Input, Variables, and Print --------------------
# Uncomment to test
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# hobby = input("Enter your favorite hobby: ")
# print(f"My name is {name}, I am {age} years old and I love {hobby}.")

# Exercise 6: Student Info
# Uncomment to test
# student_name = input("Enter student name: ")
# roll_no = input("Enter roll number: ")
# marks = input("Enter marks: ")
# print("\n--- Student Report ---")
# print(f"Name: {student_name}")
# print(f"Roll No: {roll_no}")
# print(f"Marks: {marks}")
print("-" * 50)

# -------------------- 7. Mini Project: Simple Calculator --------------------
def calculator():
    print("=== Simple Calculator ===")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Choose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Result:", num1 + num2)
    elif choice == "2":
        print("Result:", num1 - num2)
    elif choice == "3":
        print("Result:", num1 * num2)
    elif choice == "4":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid choice.")

# Uncomment to test calculator
# calculator()

print("-" * 50)

# -------------------- 8. Practice Challenges --------------------
# Beginner Level
print("Hello World! " * 3)  # Print Hello World three times

# Sum of two constants
print("Sum of 7 and 8:", 7 + 8)

# User favorite color - uncomment to test
# favorite_color = input("Enter your favorite color: ")
# print("Your favorite color is", favorite_color)
print("-" * 50)

# Intermediate Level
sentence = "Python is fun and powerful"
print("Count of 'a':", sentence.count('a'))
print("Uppercase:", sentence.upper())
print("Stripped:", sentence.strip())

# Professional Level - Login system
def login_system():
    correct_username = "admin"
    correct_password = "1234"

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username == correct_username and password == correct_password:
        print("Access Granted")
    else:
        print("Access Denied")

# Uncomment to test login system
# login_system()

print("-" * 50)

# Extract first and last name
def name_extractor():
    full_name = input("Enter your full name: ").strip()
    parts = full_name.split()
    if len(parts) >= 2:
        print("First Name:", parts[0])
        print("Last Name:", parts[-1])
    else:
        print("Please enter both first and last name.")

# Uncomment to test name extractor
# name_extractor()

print("-" * 50)

# -------------------- END OF FILE --------------------
print("Practice file loaded successfully!")
