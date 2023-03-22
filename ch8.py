#!/usr/bin/env python3

#Script: Ops 301 Class 08 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 22 MAR 2023
#Purpose: Write a python srcipt that includes the following:
# - Assign a variable to a array of 10 strings
# - Print the 4th element of the array
# - Print the 6th to the 10th element of the array
# - Change the 7th element of the array to onion

# Main

# Create the array with 10 strings
array = ["apple", "banana", "cherry", "strawberry", "blueberry", "orange", "pineapple", "watermelon", "honeydew", "kiwi"]

# Print the 4th element of the array
print(array[3])

# Print the 6th to the 10th element of the array
print(array[5:10])

# Change the 7th element of the array to onion
array[6] = "onion"

# Strech Goal
# Use the following methods to manipulate the array append(), clear(), copy(), count(), extend(), index(), insert(), pop(), remove(), reverse(), sort() methods to modify the array

# append() adds an element to the end of the list
array.append("mango")
print(array)

# copy() returns a copy of the list
array2 = array.copy()
print(array2)

# count() returns the number of elements with the specified value
print(array.count("apple"))

# extend() adds the specified list elements to the end of the current list
array3 = ["grape", "pear"]
array.extend(array3)
print(array)

# index() returns the index of the first element with the specified value
print(array.index("pear"))

# insert() adds an element at the specified position
array.insert(0, "peach")
print(array)

# pop() removes the element at the specified position
array.pop(0)
print(array)

# remove() removes the first item with the specified value
array.remove("pear")
print(array)

# reverse() reverses the order of the list
array.reverse()
print(array)

# sort() sorts the list
array.sort()
print(array)



# clear() removes all the elements from the list
array.clear()
print(array)

# End