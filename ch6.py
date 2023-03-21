#Script: Ops 301 Class 06 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 20 MAR 2023
#Purpose: Using Python module "os" create a script that executes the following tasks:
# whoami
# - ip a
# - lshw -short
# - each one should be contain in a variable
# Python function print() must be used at least 3 times to display the output of the commands

#Main

# import os module
import os

# create variables for each command
whoami = os.popen('whoami').read()
ip = os.popen('ip a').read()
lshw = os.popen('lshw -short').read()

# print the output of each command
print(whoami)
print(ip)
print(lshw)

# streach goal  - use "subprocess" instead of "os"

# import subprocess module
import subprocess

# create variables for each command
whoami = subprocess.run(['whoami'], capture_output=True)
ip = subprocess.run(['ip', 'a'], capture_output=True)
lshw = subprocess.run(['lshw', '-short'], capture_output=True)

# print the output of each command
print(whoami.stdout)
print(ip.stdout)
print(lshw.stdout)

#End