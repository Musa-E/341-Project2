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



def commandDriver(userChoice, dbConn):

    # If the input is 1-5, execute the relevant processes
    if (userChoice == '1'):
        nameSearch = input("Enter lobbyist name (first or last, wildcards _ and % supported): ")
        objecttier.get_lobbyists(dbConn, nameSearch)

    elif (userChoice == '2'):
        # station_Search_Percentages(dbConn)
        print("Command #2 has not been implemented yet.\nExiting...\n")
        exit(0)

    elif (userChoice == '3'):
        # weekdayRidershipByName(dbConn)
        print("Command #3 has not been implemented yet.\nExiting...\n")
        exit(0)

    elif (userChoice == '4'):
        # stopsInLineAndDirection(dbConn)
        print("Command #4 has not been implemented yet.\nExiting...\n")
        exit(0)

    elif (userChoice == '5'):
        # stopsByColor_DirectionSorted(dbConn)
        print("Command #5 has not been implemented yet.\nExiting...\n")
        exit(0)

    # If the user wants to exit
    elif (userChoice == 'x'):
        # print("\nExiting...")
        exit(0)
    
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
