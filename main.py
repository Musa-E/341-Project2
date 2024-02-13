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

##################################################################  
#
# main
#
print('** Welcome to the Chicago Lobbyist Database Application **')

print("Please enter a command (1-5, x to exit): ")
print("**Error, unknown command, try again...")

#
# done
#
