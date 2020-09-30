#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : luis-eduardo@dsv.su.se
# Created Date: 2020/06/23
# =============================================================================
"""
Course: Data Mining for Computer and Systems Sciences
Lab 0: Introduction to Python
Basic commands to program in Python
"""
# =============================================================================
# Imports
# =============================================================================

import my_functions

# =============================================================================
# Main
# =============================================================================

__author__ = 'Luis Quintero'
__course__ = 'Data Mining for Computer and Systems Sciences'
__date__ = '2020/06/23'
__description__ = 'Lab 0: Introduction to Python'

print('# ' + '=' * 78)
print('Author: ' + __author__)
print('Course: ' + __course__)
print('Date: ' + __date__)
print('Description: ' + __description__)
print('# ' + '=' * 78)

# Call a function Print with special characters thanks to UTF-8 encoding
print("This is a sample text to introduce Python programming... Hej då!")

print(10 + 5)

# Basic arithmetic operations
print("10 + 5 =", 10 + 5)      # Addition
print("10 - 3 =", 10 - 3)      # Substraction
print("10 * 3 =", 10 * 3)      # Multiplication
print("10 / 2 =", 10 / 2)      # Division
print("10 % 3 =", 10 % 3)      # Modulus
print("10 ** 2 =", 10 ** 2)    # Exponentiation
print("10 // 3 =", 10 // 3)    # Floor division

# Variables
x = "DAMI Course"
print(x)
print("The name of the course is", x)

x = 10
print(x)

## Invalid variable names
# 2x = 20
# my-variable = 10
# my variable = 10

# Data Types
x = True
print(x)
print(type(x))
x = False                   # Bool
print(type(x))
x = "DAMI Course"           # String (Double quotes)
print(type(x))
x = 'Intro to Python'       # String (Single quotes)
print(type(x))
x = 20                      # Integer
print(type(x))
x = 20.5                    # Floating point
print(type(x))

# Type conversion (Parsing)
x = 23.4
y = int(x)

print(type(x))
print(type(y))
print(x)
print(y)

# From string to float
x = "34.56"
y = float(x)
print(type(x))
print(type(y))

# Bool
print( 100>90 )
print( 100<90 )
print( 100 == 90)

my_age = 25
your_age = 27

if (my_age > your_age):
    print("I am older than you!")
else:
    print("I am not older than you!")

if (my_age > your_age):
    print("I am older than you!")
elif (my_age == your_age):
    print("We are both the same age!")
else:
    print("You are older than me!")

my_functions.compare_age(23, 45)

### Data Structures
# List
letters = ["A","B","C","D"]
print(letters[0])
print(letters[2])
print(letters[-2])     # Negative Indexing
print(letters[1:3])    # Range of Indexes (Slicing)

letters.append("E")
print(letters)
letters.pop(2)
more_letters = ["F","G"]

print(letters + more_letters)# Concatenate

# List with elements of different type
list_mult_types = [1, "text", False] 
print(len(list_mult_types))

# Iterate over elements of a list
for el in list_mult_types:
    print("Element:", el, "is type", type(el))

N = len(list_mult_types)    # Length of the list
print(N)
print(range(N))

for i in range(N):
    print("Element:", el, "is type", type(el))


# Strings are also arrays
first_name = "Max"
last_name = "Larsson"

print(first_name[0])
full_name = first_name + " " + last_name
print(full_name)
print(full_name.strip())
print(full_name.lower())


# Dictionary

patient = { "Full name": "Anna Smith",
            "Age": 31,
            "Nationalities": ["Swedish","American"] }

# Iterate over values
for detail in patient.values():
    print(detail)

# Iterate over keys and values
for key,value in patient.items():
    print(key,":",value)

# Access to specific value
print(patient["Age"])