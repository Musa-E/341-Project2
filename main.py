#
# Author: Musa Elqaq
# Class: CS 341, Spring 2024
#
# Program 2 - Chicago Lobbyist Database App
#
# The goal of this project is to write a console-based database 
# application in Python, this time using an N-tier design. The 
# database used for this project consists of information pertaining 
# to registered lobbyists in Chicago, their employers, their clients, 
# and their compensation.

import sqlite3
import objecttier

def print_stats(dbConn):

    print("General Statistics:")
    # Invalid Database Connection
    if (dbConn is None):
        print()
        return None

    # Call the object tier's functions
    print(f" Number of Lobbyists: {objecttier.num_lobbyists(dbConn):,}")
    print(f" Number of Employers: {objecttier.num_employers(dbConn):,}")
    print(f" Number of Clients: {objecttier.num_clients(dbConn):,}")

    # End print_stats()



def lobbyistSearch(dbConn):

    # Get input + object based on said input
    nameSearch = input("Enter lobbyist name (first or last, wildcards _ and % supported): ")
    
    return objecttier.get_lobbyists(dbConn, nameSearch)
    # End lobbyistSearch()



def lobbiystLookup(dbConn):

    # Get input + object based on said input
    IDSearch = input("Enter Lobbyist ID: ")

    return objecttier.get_lobbyist_details(dbConn, IDSearch)
    # End lobbiystLookup()



def topLobbyists(dbConn):

    # Get input
    nVal = input("Enter the value of N: ")
    
    # If N val is a digit, check if it's a positive value
    if (nVal.isdigit()):

        # Convert and confirm a valid N value
        nVal = int(nVal)
        if (nVal <= 0):
            print("Please enter a positive value for N...\n")
            return []
    
    # A dgit wasn't entered, return an empty list
    else:
        print("Please enter a positive value for N...\n")
        return []

    # Ask for a year + get an object
    yearVal = input("Enter the year: ")

    return objecttier.get_top_N_lobbyists(dbConn, nVal, yearVal)

    # End topLobbyists()



def addLobbyistYear(dbConn):

    newYear = input("Enter year: ")
    IDtoModify = input("Enter the lobbyist ID: ")
   
    return objecttier.add_lobbyist_year(dbConn, IDtoModify, newYear)

    # End addLobbyistYear()



def modifySalutation(dbConn):

    IDtoModify = input("Enter the lobbyist ID: ")
    newSalutation = input("Enter the salutation: ")
    
    return objecttier.set_salutation(dbConn, IDtoModify, newSalutation)

    # End modifySalutation()



# Handles each command's flow based on user input
def commandDriver(userChoice, dbConn):

    # If the input is 1-5, execute the relevant processes
    if (userChoice == '1'):
        lobbyistSearch(dbConn)
        
    elif (userChoice == '2'):
        lobbiystLookup(dbConn)

    elif (userChoice == '3'):
        topLobbyists(dbConn)
        
    elif (userChoice == '4'):
        addLobbyistYear(dbConn)

    elif (userChoice == '5'):
        modifySalutation(dbConn)

    # If the user wants to exit
    elif (userChoice == 'x'):
        print()
        exit(0)
    
    # Temporary functionality that allows a user to delete a year for a lobbyist
    # This is offered as an "undo-button" for command 4, and will be commented out,
    # but remain in the file.  If you want to use it, uncomment this section and
    # the relevant function in objecttier.py (used below), plug-and-play style.
    elif (userChoice == '6'):
        delYear = input('\033[91m' + '\033[1m' + "TEMP CMD - DELETE a Year: " + '\033[0m')
        IDtoModify = input('\033[91m' + '\033[1m' + "Enter the lobbyist ID: " + '\033[0m')

        objecttier.delLobbyYearTEMP(dbConn, IDtoModify, delYear)

    # A valid command must be entered to continue the program
    else:
        print("**Error, unknown command, try again...")
        userChoice = input("\nPlease enter a command (1-5, x to exit): ")
        commandDriver(userChoice, dbConn)



##################################################################  
#
# main
#
def main():

    print('** Welcome to the Chicago Lobbyist Database Application **')
    dbConn = sqlite3.connect('Chicago_Lobbyists.db');

    if (dbConn != None):
        print_stats(dbConn);

    # print()
    userChoice = input("Please enter a command (1-5, x to exit): ")
    commandDriver(userChoice, dbConn)

    # Keep looping for user input until they want to exit
    while (userChoice != 'x'):
    
        userChoice = input("Please enter a command (1-5, x to exit): ")
        commandDriver(userChoice, dbConn)


    

    #
    # done
    #

main()
