#!/bin/bash

#Script: Ops 301 Class 03 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 15 MAR 2023 
#Purpose: Create a script that accomplish the following:
#  Prompt user for input directory path
#  Promot user for input permission number
#  Navigate to directory input and changes all files to permission input
#  Finally prints the directory contents and the new permissions settings

#Main

# prompt user with input and navigates to folder
read -p "Enter the directory you want to navigate to: " dir_path

cd "$dir_path"

options=("Read/Write/execute (777)" "Read/Write/execute for owner, Read/execute for group and others (755)" "Read/Writefor owner, Read only for group and others (644)" "Read/Write for owner, No Access for group and others (600)" "Exit")

# promts user to choose with options to change permissions
echo "Select a permision option:"
    
select option in "${options[@]}"; do

    case $option in 
        "Read/Write/execute (777)")
            perm_number="777"
            break
            ;;
        "Read/Write/execute for owner, Read/execute for group and others (755)")
            perm_number="755"
            break
            ;;
        "Read/Writefor owner, Read only for group and others (644)")
            perm_number="644"
            break
            ;;
        "Read/Write for owner, No Access for group and others (600)")
            perm_number="600"
            break
            ;;
        "Exit")
            exit 0
            ;;            
        *)
            echo "You are not allowed to use that"
            ;;
    esac
done

# change the permission based on input
chmod -R "$perm_number" "$dir_path"

# print directory contents and new permission settings
echo "You have updated the permission of the following files:"
ls -l

# Stretch


#End