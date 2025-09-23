"""
Practical Exercises: Identifying and Resolving Errors in Python
---------------------------------------------------------------
This script covers:
1. Syntax Errors
2. Runtime Errors
3. Semantic Errors
"""

# -----------------------------
# 1. SYNTAX ERRORS
# -----------------------------
# Syntax errors occur when Python cannot understand the code because it violates the rules of the language.

print("\n--- SYNTAX ERROR EXERCISES ---\n")

# Example 1: Missing colon (Error)
# Uncomment to see the error
# if True
#     print("Hello")

# Corrected version:
if True:
    print("Hello - Syntax fixed!")

# Exercise: Fix the following syntax errors
# Uncomment, fix, and run each one

# print("Hello World"     # Missing closing parenthesis
# print("Python is fun!")

# def greet(name)          # Missing colon
#     print("Hello,", name)

# for i in range(5)        # Missing colon
#     print(i)

# -----------------------------
# 2. RUNTIME ERRORS
# -----------------------------
# Runtime errors occur while the program is running (after syntax checking).

print("\n--- RUNTIME ERROR EXERCISES ---\n")

# Example 2: Division by zero (Error)
# Uncomment to see the error
# num = 5 / 0

# Corrected version with error handling
try:
    num = 5 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Example 3: Using an undefined variable
# Uncomment to see the error
# print(result)

# Corrected version
result = 10
print("Result =", result)

# Exercise: Fix the runtime errors

# 1. Convert user input to an integer before performing arithmetic
# Uncomment and fix
# user_input = input("Enter a number: ")
# print("Double the number is:", user_input * 2)  # This will cause a type error if not converted

# Corrected version:
user_input = int(input("Enter a number: "))
print("Double the number is:", user_input * 2)

# 2. List index out of range
numbers = [1, 2, 3]
try:
    print(numbers[5])
except IndexError:
    print("Error: List index out of range!")

# -----------------------------
# 3. SEMANTIC ERRORS
# -----------------------------
# Semantic errors occur when the program runs but does not do what you expect.

print("\n--- SEMANTIC ERROR EXERCISES ---\n")

# Example 4: Area of a rectangle
# The formula should be length * width, but let's say we mistakenly add them
length = 5
width = 10

# Wrong (semantic error)
wrong_area = length + width
print("Wrong area of rectangle:", wrong_area)

# Correct
correct_area = length * width
print("Correct area of rectangle:", correct_area)

# Exercise: Fix semantic errors
# Problem 1: Calculate the average of three numbers
a, b, c = 10, 20, 30

# Wrong logic: adding but not dividing by 3
average_wrong = a + b + c
print("Wrong average:", average_wrong)

# Correct logic
average_correct = (a + b + c) / 3
print("Correct average:", average_correct)

# Problem 2: Check if a number is even
number = 9

# Wrong logic: checking for odd instead of even
if number % 2 == 1:
    print(number, "is even (wrong)")  # Wrong message

# Corrected version
if number % 2 == 0:
    print(number, "is even (correct)")
else:
    print(number, "is odd")

# -----------------------------
# Summary
# -----------------------------
print("\n--- SUMMARY ---")
print("Syntax Errors: Fixed before code runs (e.g., missing colon, parentheses).")
print("Runtime Errors: Occur while code is running (e.g., divide by zero, wrong index).")
print("Semantic Errors: Code runs but produces wrong results due to incorrect logic.")
