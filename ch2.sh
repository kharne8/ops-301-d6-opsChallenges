#!/bin/bash

#Script: Ops 301 Class 02 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 14 MAR 2023
#Purpose: Create a bash script that copies /var/log/syslog to the current directory and appends the current date to the file name.


#Main

cp /var/log/syslog ./syslog-$(date +%m-%d-%Y).log




#End