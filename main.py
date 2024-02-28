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
    print(f"  Number of Lobbyists: {objecttier.num_lobbyists(dbConn):,}")
    print(f"  Number of Employers: {objecttier.num_employers(dbConn):,}")
    print(f"  Number of Clients: {objecttier.num_clients(dbConn):,}")

    # End print_stats()



def lobbyistSearch(dbConn):

    # Get input + object based on said input
    nameSearch = input("\nEnter lobbyist name (first or last, wildcards _ and % supported): ")
    
    lobbyistList = objecttier.get_lobbyists(dbConn, nameSearch)

    print("\nNumber of lobbyists found:", len(lobbyistList))

    # If there are more than 100 matches, display error message and prompt user to narrow search
    if (len(lobbyistList) > 100):
        print("\nThere are too many lobbyists to display, please narrow your search and try again...\n")
        return

    # Loop through each lobbyist, even if 0 there's shouldn't be a problem
    for lobbyist in lobbyistList:
        print(lobbyist.Lobbyist_ID, ": " + lobbyist.First_Name, lobbyist.Last_Name + " Phone:", lobbyist.Phone)

    print() # Formatting

    # End lobbyistSearch()



def lobbiystLookup(dbConn):

    # Get input + object based on said input
    IDSearch = input("\nEnter Lobbyist ID: ")   

    result = objecttier.get_lobbyist_details(dbConn, IDSearch)

    if (result is not None):

        print()
        print(result.Lobbyist_ID, ":")

        # Output
        print("  Full Name: " + result.Salutation, result.First_Name, result.Middle_Initial, result.Last_Name, result.Suffix)
        print("  Address: " + result.Address_1, result.Address_2, ",", result.City + " , " + result.State_Initial, result.Zip_Code, result.Country)
        print("  Email: " + result.Email)
        print("  Phone: " + result.Phone)
        print("  Fax: " + result.Fax)
        print("  Years Registered:", end=' ')

        # Display all years the lobbyist is registered
        for i in range(0, len(result.Years_Registered)):
            print(result.Years_Registered[i], end=', ')

        # Display each employer
        print("\n  Employers:", end=' ')
        for i in range(0, len(result.Employers)):
            print(f"{result.Employers[i]}", end=", ")

        print(f"\n  Total Compensation: ${result.Total_Compensation:,.2f}")
        print() # Formatting
    else:
        print("\nNo lobbyist with that ID was found.\n")

    # End lobbiystLookup()



def topLobbyists(dbConn):

    # Get input
    nVal = input("\nEnter the value of N: ")
    
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

    result = objecttier.get_top_N_lobbyists(dbConn, nVal, yearVal)

    if (result is not None):

        # print("\nTop", nVal, "Lobbyists for", yearVal, ":\n")

        lobbyistCount = 1
        print()
        for currLobbyist in result:
            print(f"{lobbyistCount} .", currLobbyist.First_Name, currLobbyist.Last_Name)
            print("  Phone:", currLobbyist.Phone)
            print(f"  Total Compensation: ${currLobbyist.Total_Compensation:,.2f}")

            print("  Clients:", end=' ')

            # Iterate through client list:
            # print("Client count:", len(currLobbyist.Clients))

            for j in range(0, len(currLobbyist.Clients)):
                print(f"{currLobbyist.Clients[j]}", end=', ')
            
            print()
            lobbyistCount = lobbyistCount + 1
    
    print()

    # print(N, "lobbyists listed:\n")
    # print()

    # End topLobbyists()



def addLobbyistYear(dbConn):

    newYear = input("\nEnter year: ")
    IDtoModify = input("Enter the lobbyist ID: ")
   
    result = objecttier.add_lobbyist_year(dbConn, IDtoModify, newYear)

    if (result == 1): # Successfully added year to given lobbyist
        print("\nLobbyist successfully registered.\n")

    else: # adding a year to the given lobbyist has failed for some reason
        print("\nNo lobbyist with that ID was found.")

    # End addLobbyistYear()



def modifySalutation(dbConn):

    print()
    IDtoModify = input("Enter the lobbyist ID: ")
    newSalutation = input("Enter the salutation: ")
    
    result = objecttier.set_salutation(dbConn, IDtoModify, newSalutation)

    if (result):
        print("\nSalutation successfully set.\n")
    else:
        print("set_salutation failed")

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
        # print()
        exit(0)
    
    # Temporary functionality that allows a user to delete a year for a lobbyist
    # This is offered as an "undo-button" for command 4, and will be commented out,
    # but remain in the file.  If you want to use it, uncomment this section and
    # the relevant function in objecttier.py (used below), plug-and-play style.
    # elif (userChoice == '6'):
    #     delYear = input('\033[91m' + '\033[1m' + "TEMP CMD - DELETE a Year: " + '\033[0m')
    #     IDtoModify = input('\033[91m' + '\033[1m' + "Enter the lobbyist ID: " + '\033[0m')

    #     objecttier.delLobbyYearTEMP(dbConn, IDtoModify, delYear)

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

    print('** Welcome to the Chicago Lobbyist Database Application **\n')
    dbConn = sqlite3.connect('Chicago_Lobbyists.db');

    if (dbConn != None):
        print_stats(dbConn);

    # print()
    userChoice = input("\nPlease enter a command (1-5, x to exit): ")
    commandDriver(userChoice, dbConn)

    # Keep looping for user input until they want to exit
    while (userChoice != 'x'):
    
        userChoice = input("Please enter a command (1-5, x to exit): ")
        commandDriver(userChoice, dbConn)


    

    #
    # done
    #

main()
