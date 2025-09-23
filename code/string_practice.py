# ==============================================
# String Formatting and Manipulation Exercises
# ==============================================

# Sample string
text = "  Python programming is fun and powerful.  "
print("Original text:", repr(text))
print("-" * 50)

# 1. upper() - Convert to uppercase
def exercise_upper():
    result = text.upper()
    print("Uppercase:", result)

exercise_upper()
print("-" * 50)

# 2. lower() - Convert to lowercase
def exercise_lower():
    result = text.lower()
    print("Lowercase:", result)

exercise_lower()
print("-" * 50)

# 3. count() - Count occurrences of a substring
def exercise_count():
    count_python = text.count("Python")
    count_o = text.count("o")
    print("Count of 'Python':", count_python)
    print("Count of 'o':", count_o)

exercise_count()
print("-" * 50)

# 4. strip() - Remove extra spaces from both ends
def exercise_strip():
    stripped_text = text.strip()
    print("Stripped text:", repr(stripped_text))

exercise_strip()
print("-" * 50)

# 5. lstrip() and rstrip()
def exercise_lstrip_rstrip():
    left_stripped = text.lstrip()
    right_stripped = text.rstrip()
    print("Left stripped:", repr(left_stripped))
    print("Right stripped:", repr(right_stripped))

exercise_lstrip_rstrip()
print("-" * 50)

# 6. replace() - Replace a word with another
def exercise_replace():
    new_text = text.replace("Python", "Java")
    print("After replace:", new_text)

exercise_replace()
print("-" * 50)

# 7. split() - Split into a list of words
def exercise_split():
    words = text.split()
    print("Split text:", words)

exercise_split()
print("-" * 50)

# 8. join() - Join list of words into a single string
def exercise_join():
    words = ["Python", "is", "awesome"]
    joined_text = "-".join(words)
    print("Joined text:", joined_text)

exercise_join()
print("-" * 50)

# 9. Substring using slicing
def exercise_substring():
    stripped_text = text.strip()
    print("Original stripped text:", stripped_text)
    print("Substring [0:6]:", stripped_text[0:6])  # "Python"
    print("Substring [7:18]:", stripped_text[7:18]) # "programming"

exercise_substring()
print("-" * 50)

# 10. index() - Find the position of a substring
def exercise_index():
    stripped_text = text.strip()
    index_of_fun = stripped_text.index("fun")  # Throws error if not found
    print("Index of 'fun':", index_of_fun)

exercise_index()
print("-" * 50)

# 11. find() - Find position safely (no error if not found)
def exercise_find():
    stripped_text = text.strip()
    index_of_java = stripped_text.find("Java")
    print("Index of 'Java':", index_of_java)  # Returns -1 if not found

exercise_find()
print("-" * 50)

# 12. Negative indexing
def exercise_negative_index():
    stripped_text = text.strip()
    print("Last character:", stripped_text[-1])
    print("Second last character:", stripped_text[-2])
    print("Last 5 characters:", stripped_text[-5:])

exercise_negative_index()
print("-" * 50)

# 13. Replace all spaces with underscores and count underscores
def exercise_combined():
    stripped_text = text.strip()
    replaced = stripped_text.replace(" ", "_")
    print("Replaced spaces with underscores:", replaced)
    print("Count of underscores:", replaced.count("_"))

exercise_combined()
print("-" * 50)

# 14. Complex example combining split, join, and upper
def exercise_complex():
    stripped_text = text.strip()
    words = stripped_text.split()  # Convert to list
    upper_words = [word.upper() for word in words]  # Make each word uppercase
    joined = " | ".join(upper_words)  # Join with separator
    print("Formatted text:", joined)

exercise_complex()
print("-" * 50)

# 15. Practice challenge - reverse each word
def exercise_reverse_each_word():
    stripped_text = text.strip()
    words = stripped_text.split()
    reversed_words = [word[::-1] for word in words]  # Reverse each word
    result = " ".join(reversed_words)
    print("Reversed each word:", result)

exercise_reverse_each_word()
print("-" * 50)
