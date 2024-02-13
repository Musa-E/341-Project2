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
    
    dbCursor = dbConn.cursor()
    
    Lobbyists = dbCursor.execute("""
        SELECT
            COUNT(DISTINCT LobbyistAndEmployer.Lobbyist_ID) As Lobbyists
        FROM
            LobbyistAndEmployer;
    """)


    if (Lobbyists is not None):
        row = Lobbyists.fetchone()
        print("  Number of Lobbyists:", f"{row[0]:,}")


    Employers = dbCursor.execute("""
        SELECT
            COUNT(DISTINCT EmployerInfo.Employer_ID) AS Employers
        FROM
            EmployerInfo
        LEFT JOIN
            LobbyistAndEmployer ON EmployerInfo.Employer_ID = LobbyistAndEmployer.Employer_ID;
    """);

    if (Employers is not None):
        row = Employers.fetchone()
        print("  Number of Employers:", f"{row[0]:,}")


    Clients = dbCursor.execute("""
        SELECT
            COUNT(DISTINCT ClientInfo.Client_ID) As Clients
        FROM
            ClientInfo;                                       
    """)

    if (Clients is not None):
        row = Clients.fetchone()
        print("  Number of Clients:", f"{row[0]:,}")

    # Get the result
    # if (result is not None):

    #     rows = result[0]
        
    #     return result.fetchall()
    # else:
    #     return ()



def commandDriver(userChoice, dbConn):

    # If the input is 1-5, execute the relevant processes
    if (userChoice == '1'):
        print("Command #1 has not been implemented yet.\nExiting...\n")
        exit(0)

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
