# Assignment
# ------------------------------------------------------------
# '=' assigns the value on the right side to the variable on the left side.

score = 50
print(score)


# Reassignment
# ------------------------------------------------------------
# Reassignment means assigning a new value to an existing variable.

score = 50
print(score)  # Output: 50

score = 90
print(score)  # Output: 90


# Reassignment with Different Type
# ------------------------------------------------------------
# A variable can point to a different type after reassignment.

value = 100
print(value)  # Output: 100

value = "One hundred"
print(value)  # Output: One hundred


# Multiple Assignment (Same value)
# ------------------------------------------------------------
# We can assign the same value to multiple variables in one line.

a = b = c = 100
print(a, b, c)  # Output: 100 100 100


# Multiple Assignment (Different values)
# ------------------------------------------------------------
# We can assign different values to multiple variables in one line.

name, age, city = "Sakib", 22, "Beijing"

print(name, age, city)  # Output: Sakib 22 Beijing


# One Value to Multiple Variables with None
# ------------------------------------------------------------
# None means no value or empty value.

x = y = z = None

print(x)  # Output: None
print(y)  # Output: None
print(z)  # Output: None


# Multiple Assignment with Different Types
# ------------------------------------------------------------
# Different variables can receive different types of values.

x, y, z = 1, 2.5, "Python"

print(x, y, z)  # Output: 1 2.5 Python


# Count Must Match
# ------------------------------------------------------------
# The number of variables must match the number of values.

a, b, c = 10, 20, 30

print(a, b, c)  # Output: 10 20 30

# Wrong examples:
# a, b = 10, 20, 30
# Output: ValueError, because there are too many values to unpack.

# a, b, c = 10, 20
# Output: ValueError, because there are not enough values to unpack.


# List Unpacking
# ------------------------------------------------------------
# Unpacking means assigning values from a collection to variables.

fruits = ["apple", "banana", "cherry"]

x, y, z = fruits

print(x)  # Output: apple
print(y)  # Output: banana
print(z)  # Output: cherry


# Tuple Unpacking
# ------------------------------------------------------------
# Tuple values can also be unpacked.

coordinates = (10, 20)

x, y = coordinates

print(x)  # Output: 10
print(y)  # Output: 20


# Unpacking Mixed Data
# ------------------------------------------------------------
# A collection can contain different types of values.

data = ["Apple", 2, 4.2]

item_name, quantity, price = data

print(item_name)  # Output: Apple
print(quantity)  # Output: 2
print(price)  # Output: 4.2


# Unpacking is Similar to Index Access
# ------------------------------------------------------------
# These two ideas are similar.

data = ["Apple", 2, 4.2]

a = data[0]
b = data[1]
c = data[2]

print(a, b, c)  # Output: Apple 2 4.2

x, y, z = data

print(x, y, z)  # Output: Apple 2 4.2


# Asterisk Unpacking
# ------------------------------------------------------------
# The * symbol can collect remaining values into a list.

first, *rest = [2, 4, 6, 8, 10]

print(first)  # Output: 2
print(rest)  # Output: [4, 6, 8, 10]


# Asterisk Unpacking in the Middle
# ------------------------------------------------------------
# The * variable collects all middle values.

first, *middle, last = [1, 2, 3, 4, 5]

print(first)  # Output: 1
print(middle)  # Output: [2, 3, 4]
print(last)  # Output: 5


# Asterisk Unpacking at the Beginning
# ------------------------------------------------------------
# The * variable can also collect starting values.

*start, last = [10, 20, 30, 40]

print(start)  # Output: [10, 20, 30]
print(last)  # Output: 40


# Swapping Two Variables
# ------------------------------------------------------------
# Python can swap values without a temporary variable.

a = 5
b = 10

a, b = b, a

print(a)  # Output: 10
print(b)  # Output: 5


# Normal Swapping Method
# ------------------------------------------------------------
# This is how swapping is done in many other languages.

a = 5
b = 10

temp = a
a = b
b = temp

print(a)  # Output: 10
print(b)  # Output: 5


# Deleting Variables with del
# ------------------------------------------------------------
# del removes the variable name.

x = 10

print(x)  # Output: 10

del x

# print(x)
# Output: NameError, because x is deleted and no longer exists.
