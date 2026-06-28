# Scope means where a variable can be used/accessed.
# ------------------------------------------------------------
# 1. Local scope → inside function
# 2. Global scope → outside function


# Local Variable
# ------------------------------------------------------------
# A local variable is created inside a function.
# It can only be used inside that function.


def local_example():
    name = "Rohan"
    print("Inside function:", name)


local_example()
# Output: Inside function: Rohan

# print(name)
# Output: NameError, because name exists only inside local_example().


# Global Variable
# ------------------------------------------------------------
# A global variable is created outside all functions.
# It can be used outside a function.
# It can also be read inside a function.

language = "Python"


def global_example():
    print("Inside function:", language)


global_example()
# Output: Inside function: Python

print("Outside function:", language)
# Output: Outside function: Python


# Local and Global Variable with Same Name
# ------------------------------------------------------------
# If a local variable and a global variable have the same name,
# Python uses the local variable inside the function.
# The global variable stays unchanged outside the function.

x = "global"


def same_name_example():
    x = "local"
    print("Inside function:", x)


same_name_example()
# Output: Inside function: local

print("Outside function:", x)
# Output: Outside function: global

# Explanation:
# Inside the function, x means the local x.
# Outside the function, x means the global x.


# Reading a Global Variable
# ------------------------------------------------------------
# Reading a global variable inside a function does not need global keyword.

count = 10


def show_count():
    print("Count is:", count)


show_count()
# Output: Count is: 10


# Changing a Global Variable
# ------------------------------------------------------------
# If we want to change a global variable inside a function,
# we must use the global keyword.

score = 0


def update_score():
    global score
    score = 100
    print("Inside function:", score)


update_score()
# Output: Inside function: 100

print("Outside function:", score)
# Output: Outside function: 100


# Without global Keyword
# ------------------------------------------------------------
# If we assign a value inside a function without global,
# Python creates a new local variable.

status = "old"


def change_status_without_global():
    status = "new"
    print("Inside function:", status)


change_status_without_global()
# Output: Inside function: new

print("Outside function:", status)
# Output: Outside function: old

# Explanation:
# The status inside the function is local.
# The global status remains unchanged.


# With global Keyword
# ------------------------------------------------------------
# global tells Python: "Use the global variable, not a new local variable."

status = "old"


def change_status_with_global():
    global status
    status = "new"
    print("Inside function:", status)


change_status_with_global()
# Output: Inside function: new

print("Outside function:", status)
# Output: Outside function: new

# Explanation: This time the global status was changed.


# Creating a Global Variable Inside a Function
# ------------------------------------------------------------
# If we use global inside a function,
# we can create a global variable from inside the function.
# This is possible, but not recommended for normal beginner code.


def create_global_variable():
    global country
    country = "Bangladesh"


create_global_variable()

print(country)
# Output: Bangladesh


# Multiple Global Variables
# ------------------------------------------------------------
# We can use global with multiple variable names, But use this carefully.

x = y = z = None

data = ["Apple", 2, 4.2]


def assign_globals():
    global x, y, z
    x, y, z = data


assign_globals()

print(x)  # Output: Apple
print(y)  # Output: 2
print(z)  # Output: 4.2


# Local Variable Lifetime
# ------------------------------------------------------------
# A local variable exists only while the function is running.
# After the function finishes, the local variable is gone.


def temporary_data():
    temp = "I exist only inside this function"
    print(temp)


temporary_data()
# Output: I exist only inside this function

# print(temp)
# Output: NameError, because temp does not exist outside the function.


# Final Memory Rule
# ------------------------------------------------------------
# Local variable:
# Created inside a function.
# Used only inside that function.

# Global variable:
# Created outside all functions.
# Can be read inside and outside functions.

# Avoid changing global variables too much.
# Too many global variables can make code confusing.

# Reading global variable  -> no global keyword needed
# Changing global variable -> global keyword needed
