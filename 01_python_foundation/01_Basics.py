# What is Python?
# ------------------------------------------------------------
# Python is a high-level programming language.
# It is used to give instructions to a computer.

print("Python is a programming language")


# Python Applications
# ============================================================
# Python is used in many real-world areas:

print("AI and Machine Learning")
print("Web Development")
print("Data Science")
print("Automation")
print("Backend Development")


# How Python Runs
# ------------------------------------------------------------
# Python code is written in .py files. Examples: hello.py, main.py
# Python executes code line by line from top to bottom using the interpreter.

print("Python executes code from top to bottom")


# First Python Program
# ------------------------------------------------------------
print("Hello, World!")  # Output: Hello, World!


# print() Function
# ============================================================
# print() is used to display output on the screen.

print("Hello")
print("World")

# Printing numbers
print(25)

# Printing text and numbers together
print("I am", 25, "years old")


# Python Statements
# ------------------------------------------------------------
# A statement is a complete instruction that Python can execute.
# Python runs statements one by one in order (top to bottom).

print("Statement 1")
print("Statement 2")
print("Statement 3")

# Each print() here is a separate statement.
# Python executes them sequentially.


# Comments
# ============================================================
# Comments are ignored by Python.

print("Comments help understanding code")

# This line will not run:
# print("This is commented out")


# Expression vs Statement
# ------------------------------------------------------------
# Expression = part of code that produces a value
# Statement = complete instruction executed by Python

x = 10 + 5

# 10 + 5 is an expression.
# Because it produces the value 15.

# x = 10 + 5 is a statement.
# Because this full line tells Python: "Calculate 10 + 5 and store the result in x."

print(x)  # Output: 15

# 10 + 5         --> Expression
# x = 10 + 5     --> Statement
# print(x)       --> Statement
# print(10 + 5)  --> Statement using an expression inside it


# Indentation
# ------------------------------------------------------------
# Python uses indentation (spaces) to define blocks of code.
# Indentation means spaces at the beginning of a line.

if True:
    print("This line is indented")
    print("This is also inside the block")

# Wrong indentation causes error:
# if True:
# print("This will cause IndentationError")


# Syntax Error Intro
# ------------------------------------------------------------
# Syntax means rules of writing code.
# Wrong syntax causes SyntaxError.

print("Correct syntax")

# Wrong syntax example:
# print("Missing parenthesis"
# Output: SyntaxError, because closing parenthesis is missing.

# Correct version:
print("No syntax error here")


# NameError Intro
# ------------------------------------------------------------
# Python treats any word without quotes as a variable name
# If it is not defined → NameError occurs

# print(Hello)
# Output: NameError, because Hello is not inside quotes.
# Python thinks Hello is a variable name.

# Correct version:
print("Hello")


# Final Rule
# ------------------------------------------------------------
# - Python is used to give instructions to a computer.
# - print() shows output
# - Expression produces a value
# - Statement executes an instruction
# - Comments are ignored
# - Indentation defines blocks
# - SyntaxError = wrong structure
# - NameError = undefined variable
