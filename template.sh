#!/bin/bash

#Script: Ops 301 Class 13 Ops Challenge Solution
#Author: Marco Aliaga
#Date of latest revision: 29 Mar 2023
#Purpose: Creatre a script that prompt user with text inputs to add new user to AC on Server Manager

#Main

#Prompt user to add a new user to AC if "yes" continue, if "no" exit
$addUser = Read-Host "Would you like to add a new user to AC? (Yes/No)"


if($addUser -eq "Yes") {

#Prompt user for first and last name and store in variables
$firstName = Read-Host "Enter the user's first name:"
$lastName = Read-Host "Enter the user's last name:"
    
#Use user inputs to create User Samaccountbname logon
$samAccountName = $firstName.Substring(0,1) + $lastName
    
# Prompt user to if it would like to continue with the SamAccountName
$continue = Read-Host "The user's SamAccountName will be $samAccountName. Would you like to continue? (Yes/No)"
    
if($continue -eq "Yes") {

#Prompt user for job title and store in variable
$jobTitle = Read-Host "Enter the user's job title:"
        
#Prompt user for department and store in variable
$department = Read-Host "Enter the user's department:"
        
#Prompt user for company and store in variable
$company = Read-Host "Enter the user's company:"
        
# Prompt user to confirm and add user or start over
Write-Host ""
Write-Host "User Details:"
Write-Host "First Name: $firstName"
Write-Host "Last Name: $lastName"
Write-Host "SamAccountName: $samAccountName"
Write-Host "Job Title: $jobTitle"
Write-Host "Department: $department"
Write-Host "Company: $company"
Write-Host ""
        
$confirm = Read-Host "Enter Yes to add user or No to enter information again"
        

# Add the user to Active Directory Administrative Center
if($confirm -eq "Yes") {
    New-ADUser -Name "$firstName $lastName" `
    -GivenName $firstName `
    -Surname $lastName `
    -SamAccountName $samAccountName `
    -UserPrincipalName "$samAccountName@yourdomain.com" `
    -Title $jobTitle `
    -Department $department `
    -Company $company `
    -AccountPassword (ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force) `
    -Enabled $true
            
    Write-Host "User added successfully."
        }
else {
            # Start over
            & $MyInvocation.MyCommand.Path
        }
    }
    else {
        # Start over
        & $MyInvocation.MyCommand.Path
    }
}
else {
    # Exit
    exit
}






#End