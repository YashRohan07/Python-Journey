# What is a Variable?
# ------------------------------------------------------------
# A variable is a name that refers to a value.
# We use variables to store data and use that data later.
# In Python, a variable does not directly store the value.
# A variable points or refers to an object/value in memory.

name = "Sakib"
age = 22
city = "Beijing"

print(name)
print(age)
print(city)


# Variable Creation
# ------------------------------------------------------------
# Variables are created when we assign a value.
# No need to declare type manually.

student_name = "Rohan"
student_age = 25


# Python is Dynamically Typed
# ------------------------------------------------------------
# Python automatically detects the type of variable.
# Do not need to write int, float, or string before variable names.

number = 100
price = 49.99
language = "Python"
is_learning = True

print(number)
print(price)
print(language)
print(is_learning)


# Type can change (Dynamic nature)
# ------------------------------------------------------------
# A variable can refer to different types at different times.

value = 10
print(value)  # Output: 10

value = "Now I am a string"
print(value)  # Output: Now I am a string


# Python is Strongly Typed
# ------------------------------------------------------------
# Python does not automatically combine different types.
# For example, int + str is not allowed unless we convert one type.

a = 5
b = "10"

# print(a + b)
# Output: TypeError, because int and string cannot be added directly.

print(a + int(b))  # Output: 15


# Variable Naming Rules
# ------------------------------------------------------------
# A variable name must start with a letter or underscore.
# A variable name cannot start with a number.
# A variable name can contain letters, numbers, and underscores.
# Variable names are case-sensitive.
# Python keywords cannot be used as variable names.

name = "John"
_user = "Alex"
user_name = "Rohan"
user2 = "Yash"

print(name, _user, user_name, user2)


# Illegal Variable Names
# ------------------------------------------------------------
# These are wrong examples.
# Keep them as comments because they will cause errors.

# 2name = "Error"
# Output: SyntaxError, because variable name cannot start with a number.

# user-name = "Error"
# Output: SyntaxError, because hyphen is not allowed.

# my var = "Error"
# Output: SyntaxError, because space is not allowed.

# class = 10
# Output: SyntaxError, because class is a Python keyword.


# Good Naming Practice
# ------------------------------------------------------------
# Use meaningful names for better readability.

product_price = 500
product_quantity = 2
total_price = product_price * product_quantity

print(total_price)


# Naming Styles
# ------------------------------------------------------------
# snake_case is recommended for Python variables and functions.
# camelCase is common in JavaScript.
# PascalCase is usually used for class names in Python.

student_name = "Sakib"  # snake_case
studentName = "Sakib"  # camelCase
StudentName = "Sakib"  # PascalCase

print(student_name)  # Output: Sakib
print(studentName)  # Output: Sakib
print(StudentName)  # Output: Sakib


# Case Sensitivity
# ------------------------------------------------------------
# Python variable names are case-sensitive.
# age, Age, and AGE are three different variables.

age = 20
Age = 30
AGE = 40

print(age)  # Output: 20
print(Age)  # Output: 30
print(AGE)  # Output: 40


# Constants Convention
# ------------------------------------------------------------
# Constants are written in ALL CAPS.
# Python will still allow changing them, but we should not change them.

PI = 3.1416
MAX_USERS = 100
DAYS_IN_WEEK = 7

print(PI)  # Output: 3.1416
print(MAX_USERS)  # Output: 100
print(DAYS_IN_WEEK)  # Output: 7

PI = 10

print(PI)  # Output: 10

# This is allowed in Python, but not recommended.
# Constants should be treated as fixed values.


# Single and Double Quotes
# ------------------------------------------------------------
# String values can use single quotes or double quotes.

first_name = "Sakib"
last_name = "Hasan"

print(first_name, last_name)


# Using + with String Variables
# ------------------------------------------------------------
# For strings, + joins strings together.
# This is called string concatenation.

x = "Python "
y = "is "
z = "awesome"

print(x + y + z)  # Output: Python is awesome


# Using + with Number Variables
# ------------------------------------------------------------
# For numbers, + performs mathematical addition.

num1 = 5
num2 = 10

print(num1 + num2)  # Output: 15


# Mixing String and Number with +
# ------------------------------------------------------------
# String + number is not allowed directly.

number = 5
person = "John"

# print(number + person)
# Output: TypeError, because int and string cannot be added directly.

print(number, person)  # Output: 5 John
