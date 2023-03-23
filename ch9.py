#!/usr/bin/env python3

#Script: Ops 301 Class 09 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 23 MAR 2023
#Purpose: Create if statments that will print a message if the following conditions are met:
# - Equals a = b
# - Not equals a != b
# - Greater than a > b
# - Less than a < b
# - Greater than or equal to a >= b
# - Less than or equal to a <= b
#  Create and if statement using logical conditional operator of your choice and include elif keyword that executes when other conditions are not met
# Create and if statement that includes both elif and else keywords to execute when other conditions are not met

# Main

# Create variables
a = 5
b = 10

# Equals a = b
if a == b:
    print("a is equal to b")

# Not equals a != b
if a != b:
    print("a is not equal to b")

# Greater than a > b
if a > b:
    print("a is greater than b")

# Less than a < b
if a < b:
    print("a is less than b")

# Greater than or equal to a >= b
if a >= b:
    print("a is greater than or equal to b")

# Less than or equal to a <= b
if a <= b:
    print("a is less than or equal to b")

# elif keyword that executes when other conditions are not met
if a == b:
    print("a is equal to b")
elif a != b:
    print("a is not equal to b")

# if statement that includes both elif and else keywords to execute when other conditions are not met
if a == b:
    print("a is equal to b")
elif a != b:
    print("a is not equal to b")
else:
    print("a is not equal to b")

# End