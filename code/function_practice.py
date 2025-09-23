# ==============================================
# Beginner to Professional Functions in Python
# ==============================================

# ----------- Beginner Level -------------------

# 1. Basic function
def greet_user():
    print("Hello, welcome to Python!")

greet_user()
print("-" * 40)

# 2. Function with one parameter
def greet(name):
    print(f"Hello, {name}!")

greet("Fawad")
print("-" * 40)

# 3. Function with two parameters
def add_numbers(a, b):
    print("The sum is:", a + b)

add_numbers(5, 10)
print("-" * 40)

# 4. Returning values
def add_and_return(a, b):
    return a + b

result = add_and_return(8, 12)
print("Returned Sum:", result)
print("-" * 40)

# 5. Default parameter
def greet_default(name="Guest"):
    print(f"Hello, {name}!")

greet_default("Ali")
greet_default()
print("-" * 40)

# 6. Multiple return values
def calculate(a, b):
    return a + b, a * b

sum_result, product_result = calculate(4, 5)
print("Sum:", sum_result, "Product:", product_result)
print("-" * 40)

# 7. Keyword arguments
def student_info(name, age, grade):
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

student_info(age=20, name="Fawad", grade="A")
print("-" * 40)

# 8. Function with loop
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(5)
print("-" * 40)

# 9. Function calling another function
def square(x):
    return x ** 2

def display_square(x):
    print(f"The square is: {square(x)}")

display_square(6)
print("-" * 40)

# 10. Lambda function
cube = lambda x: x ** 3
print("Cube of 3:", cube(3))
print("-" * 40)

# ----------- Intermediate Level -------------------

# 11. Function with a list
def find_max(numbers):
    return max(numbers)

nums = [2, 7, 1, 9, 3]
print("Max value in list:", find_max(nums))
print("-" * 40)

# 12. Recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
print("-" * 40)

# 13. Function to reverse a string
def reverse_string(s):
    return s[::-1]

print("Reverse of 'Python':", reverse_string("Python"))
print("-" * 40)

# 14. Function with *args (variable length arguments)
def sum_all(*args):
    return sum(args)

print("Sum of numbers:", sum_all(1, 2, 3, 4, 5))
print("-" * 40)

# 15. Function with **kwargs (keyword arguments)
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(Name="Fawad", Age=22, Country="Pakistan")
print("-" * 40)

# 16. Function that returns a dictionary
def student_dict(name, age, grade):
    return {
        "name": name,
        "age": age,
        "grade": grade
    }

student = student_dict("Fawad", 22, "A")
print("Student Dictionary:", student)
print("-" * 40)

# ----------- Professional Level -------------------

# 17. Menu driven program using functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def menu():
    print("\n==== Calculator Menu ====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("=========================")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "5":
        print("Exiting program. Goodbye!")
        break

    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(num1, num2))
            elif choice == "2":
                print("Result:", subtract(num1, num2))
            elif choice == "3":
                print("Result:", multiply(num1, num2))
            elif choice == "4":
                print("Result:", divide(num1, num2))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
    else:
        print("Invalid choice! Please select a valid option.")
