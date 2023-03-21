#!/usr/bin/env python3

#Script: Ops 301 Class 07 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 21 MAR 2023
#Purpose: Create a python script that generates all directories, sub-directories and files for a user-provided directory path. It must have the following:
# - Script must ask the user for a file path and read a user input string into a variable.
# - Script must use the os.walk() function from the os library.
# - Script must enclose the os.walk() function within a python function that hands it the user input file path.


# Start
# Import libraries


import os

# Declaration of variables


### Read user input here into a variable
path =  input("Enter a file path: ")

# Declaration of functions

### Declare a function here
def genDir():
    for (root, dirs, files) in os.walk(path):
    ### Add a print command here to print ==root==
        print(root)
        for dir in dirs:
        ### Add a print command here to print ==dirs==
            print(dirs)
        for file in files:
        ### Add a print command here to print ==files==
            print(files)

# Main
### Pass the variable into the function here

genDir(path)

# End
