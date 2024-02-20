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
    print("  Number of Lobbyists:", objecttier.num_lobbyists(dbConn))
    print("  Number of Employers:", objecttier.num_employers(dbConn))
    print("  Number of Clients:", objecttier.num_clients(dbConn))

    # End print_stats()



# Handles each command's flow based on user input
def commandDriver(userChoice, dbConn):

    # If the input is 1-5, execute the relevant processes
    if (userChoice == '1'):
        nameSearch = input("Enter lobbyist name (first or last, wildcards _ and % supported): ")
        LobbyistList = objecttier.get_lobbyists(dbConn, nameSearch)

    elif (userChoice == '2'):
        IDSearch = input("Enter Lobbyist ID: ")
        lobbyistDetailsObject = objecttier.get_lobbyist_details(dbConn, IDSearch)

    elif (userChoice == '3'):
        nVal = input("Enter the value of N: ")
        
        if (nVal.isdigit()):
            nVal = int(nVal)
            if (nVal <= 0):
                print("Please enter a positive value for N...\n")
                return []
        else:
            print("Please enter a positive value for N...\n")
            return []

        yearVal = input("Enter the year: ")
        objecttier.get_top_N_lobbyists(dbConn, nVal, yearVal)

    elif (userChoice == '4'):
        newYear = input("Enter year: ")
        IDtoModify = input("Enter the lobbyist ID: ")
        lobbyistDetailsObject = objecttier.add_lobbyist_year(dbConn, IDtoModify, newYear)

    elif (userChoice == '5'):
        # stopsByColor_DirectionSorted(dbConn)
        print("Command #5 has not been implemented yet.\nExiting...\n")
        exit(0)

    # If the user wants to exit
    elif (userChoice == 'x'):
        # print("\nExiting...")
        exit(0)
    
    elif (userChoice == '6'):
        delYear = input("TEMP CMD - DELETE a Year: ")
        IDtoModify = input("Enter the lobbyist ID: ")

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

    print()
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
