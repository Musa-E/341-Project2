#
# datatier.py
#
# Executes SQL queries against the given database.
#
# Original author: Prof. Joe Hummel, Ellen Kidane
#
import sqlite3


##################################################################
#
# select_one_row:
#
# Given a database connection and a SQL Select query,
# executes this query against the database and returns
# the first row retrieved by the query (or the empty
# tuple () if no data was retrieved). The query can
# be parameterized, in which case pass the values as
# a list via parameters; this parameter is optional.
#
# Returns: first row retrieved by the given query, or
#          () if no data was retrieved. If an error
#          occurs, a msg is output and None is returned.
#
def select_one_row(dbConn, sql, parameters = None):

    # Invalid Database Connection
    if (dbConn is None):
        print()
        return None

    # No query is provided
    # elif (sql is None or sql == ""):
    #     print()
    #     return None

    # Wildcards are used, but no values to fill in for them are provided
    # elif ('?' in sql or '_' in sql and parameters == None):
    #     print()
    #     return None
    
    dbCursor = dbConn.cursor()
    result = None

    if (parameters is None):
        result = dbCursor.execute(sql)
    else:
        result = dbCursor.execute(sql, parameters)

    # Get the result
    if (result is not None):

        # Return only the first row
        return result.fetchone()
    else:
        return ()

    # End select_one_row()


##################################################################
#
# select_n_rows:
#
# Given a database connection and a SQL Select query,
# executes this query against the database and returns
# a list of rows retrieved by the query. If the query
# retrieves no data, the empty list [] is returned.
# The query can be parameterized, in which case pass 
# the values as a list via parameters; this parameter 
# is optional.
#
# Returns: a list of 0 or more rows retrieved by the 
#          given query; if an error occurs a msg is 
#          output and None is returned.
#
def select_n_rows(dbConn, sql, parameters = None):
    
    # Invalid Database Connection
    if (dbConn is None):
        print()
        return None

    # No query is provided
    elif (sql is None or sql == ""):
        print("**[1] A SQL error has occured.\n")
        return None
    
    # Cursor, and get number of wildcards
    dbCursor = dbConn.cursor()
    paramCount = sql.count('?') # I only use '?' for wildcards, not '_'

    if (parameters is not None):

        # parameters = (parameters, parameters)
        if (paramCount == 0):
            parameters = (None,)

        elif (paramCount == 2): # only 1 function uses this (in this project)
            parameters = (parameters, parameters)
        
        
        # print("Param Count: ", paramCount)

        # Dynamically add to the list of parameters; caused problems, so is unimplemented
        # if paramCount == 0:
        #     parameters = (''.join(parameters),)
        #     parameters = (None,)
        # else:

        #     print("Preloop: The tuple is now: ", parameters)
        #     for i in range(0, paramCount):
        #         parameters = (''.join(parameters),)
        #         print("The tuple is now: ", parameters)

        # print("**The tuple is now: ", parameters)
        # temp = tuple(''.join(each) for each in parameters)
        # parameters = temp
    else:
        parameters = (None, None)

    # Query the database
    result = dbCursor.execute(sql, parameters)

    row = result.fetchall()
    # Get the result
    if (row is not None):

        # Return all rows
        return row
    else:
        return []
    
    # End select_n_rows()


##################################################################
#
# perform_action: 
# 
# Given a database connection and a SQL action query,
# executes this query and returns the # of rows
# modified; a return value of 0 means no rows were
# updated. Action queries are typically "insert", 
# "update", "delete". The query can be parameterized,
# in which case pass the values as a list via 
# parameters; this parameter is optional.
#
# Returns: the # of rows modified by the query; if an 
#          error occurs a msg is output and -1 is 
#          returned. Note that a return value of 0 is
#          not considered an error --- it means the
#          query did not change the database (e.g. 
#          because the where condition was false?).
#
def perform_action(dbConn, sql, parameters = None):

    # Invalid Database Connection
    if (dbConn is None):
        print()
        return -1

    # No query is provided
    elif (sql is None or sql == ""):
        print()
        return -1

    # Wildcards are used, but no values to fill in for them are provided
    elif ('?' in sql or '_' in sql and parameters == None):
        print()
        return -1
    
    dbCursor = dbConn.cursor()
    result = None

    result = dbCursor.execute(sql, parameters);

    # Commit the changes to the database
    dbConn.commit()

    # Return the number of rows modified
    return result.rowcount

    # Get the result
    # if (result is not None):

    #     # Return only the first row
    #     return result.fetchone()
    # else:
    #     return ()

    # End perform_action()
    pass
