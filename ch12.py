#!/usr/bin/env python3

#Script: Ops 301 Class 12 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 28 MAR 2023
#Purpose: Create a python script that using the requests library:
# - Prompts the user to type a string as destiantion url
# - Prompts user to select a HTTP method:
#   - GET
#   - POST
#   - PUT
#   - DELETE
#   - HEAD
#   - PATCH
#   - OPTIONS
# Print to the screen the entire request the script is about to send. Ask the user to confirm the request.
# For the given header translate the error code into a human readable error message.
# For the fiven URL print the response header to the screen

# Main

# Import requests
import requests

# Prompt user for URL
url = input("Enter a URL: ")

# Prompt user menu for HTTP method and store in variable
print("Select a HTTP method:")
print("1. GET")
print("2. POST")
print("3. PUT")
print("4. DELETE")
print("5. HEAD")
print("6. PATCH")
print("7. OPTIONS")
method = input("Enter a number: ")

# If statement to determine which HTTP method to use
if method == "1":
    method = "GET"
elif method == "2":
    method = "POST"
elif method == "3":
    method = "PUT"
elif method == "4":
    method = "DELETE"
elif method == "5":
    method = "HEAD"
elif method == "6":
    method = "PATCH"
elif method == "7":
    method = "OPTIONS"
else:
    print("Invalid input")

# Print request to screen
print("Request: " + method + " " + url)

# Prompt user to confirm request
confirm = input("Confirm request? (y/n): ")

# If statement to determine if request is confirmed
if confirm == "y":
    # If confirmed, send request
    response = requests.request(method, url)
    # Print response to screen
    print(response.text)    
else:
    # If not confirmed, print message
    print("Request not confirmed. Exiting.")

# End





# END

