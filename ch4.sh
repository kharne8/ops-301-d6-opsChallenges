#!/bin/bash

#Script: Ops 301 Class 04 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 16 MAR 2023
#Purpose: Create a bash script that prompts user with a menu and executes their input

#Main

# first define the functions that will be called after user input

function helloWorld(){
    echo "Hello World"
}

# the -c tells the ping to do it a certain amount of times in this case 8
function pingSelf(){
    ping -c 8 127.0.0.1
}

function infoIP(){
    ip a
}

# then start a while loop that show the options that will execute the functions and it will run until users chooses to exit

while true; do
    echo "Please select an option: "
    echo "1. Print Hello World"
    echo "2. Ping Self"
    echo "3. Show IP config info"
    echo "4. Exit"
    # set user input to choice variable
    read -p "Enter your choice: " choice

    # use var to call function based on input
    case $choice in
        1)
            helloWorld
            ;;
        2)
            pingSelf
            ;;
        3)
            infoIP
            ;;
        4)
            break
            ;;
    esac
done

#End