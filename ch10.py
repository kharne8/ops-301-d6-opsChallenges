#!/usr/bin/env python3

#Script: Ops 301 Class 10 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 24 MAR 2023
#Purpose: Using file handling commands, create a python script that:
# - Creates a new .txt file
# - Adds three lines of text to the file
# - Prints to the screen the fisrt line of the file
# = Deletes the .txt file

# Main

# Create a new .txt file
f = open("test.txt", "w")

# Add three lines of text to the file
f.write("This is line 1\n")
f.write("This is line 2\n")
f.write("This is line 3")

# Print to the screen the fisrt line of the file
with open("test.txt", "r") as file:
    first = file.readline()
    print(first)

# Delete the .txt file
import os
os.remove("test.txt")

# End