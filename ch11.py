#!/usr/bin/env python3

#Script: Ops 301 Class 1 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 27 MAR 2023
#Purpose: Import Psutil and create a python script that fetches the following information:
# - Time spent by normal processes executing in user mode
# - Time spent by niced processes executing in kernel mode
# - Time spent when system was idle
# - Time spent by priority processes executing in user mode
# - Time spent waiting for I/O to complete
# - Time spent for servicing hardware interrupts
# - Time spent for servicing software interrupts
# - Time spent by other operating systems running in a virtualized environment
# - Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel

# Main

# Import Psutil
import psutil

# Fetch the following information:
# - Time spent by normal processes executing in user mode
print("Time spent by normal processes executing in user mode: " + str(psutil.cpu_times().user))

# - Time spent by niced processes executing in kernel mode
print("Time spent by niced processes executing in kernel mode: " + str(psutil.cpu_times().nice))

# - Time spent when system was idle
print("Time spent when system was idle: " + str(psutil.cpu_times().idle))

# - Time spent by priority processes executing in user mode
print("Time spent by priority processes executing in user mode: " + str(psutil.cpu_times().iowait))

# Time spent waiting for I/O to complete
print("Time spent waiting for I/O to complete: " + str(psutil.cpu_times().irq))

# Time spent for servicing hardware interrupts
print("Time spent for servicing hardware interrupts: " + str(psutil.cpu_times().softirq))

# Time spent for servicing software interrupts
print("Time spent for servicing software interrupts: " + str(psutil.cpu_times().steal))

# Time spent by other operating systems running in a virtualized environment
print("Time spent by other operating systems running in a virtualized environment: " + str(psutil.cpu_times().guest))

# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
print("Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel: " + str(psutil.cpu_times().guest_nice))

# Stretch
# Save the info to a .txt file
info= open("info.txt", "w")


# End