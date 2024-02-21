#
# datatier.py
#
# Executes SQL queries against the given database.
#
# Original author: Prof. Joe Hummel, Ellen Kidane
#
# Modified By: Musa Elqaq [for CS341, Spring 2024]
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

    rows = None # Holds return vals

    # Try to connect and do stuff
    try:
        dbCursor = dbConn.cursor()
        result = None

        # If there are parameters, use them in .execute
        if (parameters is None):
            result = dbCursor.execute(sql) # Query database
        
        # Else, only use sql query
        else:
            result = dbCursor.execute(sql, parameters)
        
        rows = result.fetchone() # Store data
    
    # Catch Exceptions & return None
    except Exception as e:
        print("select_one_row failed:", e)
        return None
    
    # No matter what, close the cursor
    finally:
        dbCursor.close()


    # Get the result, if none, returns ()
    if (rows is not None):
        return rows # Return only the first row
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
    
    row = None  # init the data holder

    try:
        # Cursor, and get number of wildcards
        dbCursor = dbConn.cursor()

        # If there are parameters, use them in the .execute
        if (parameters is not None):
            
            result = dbCursor.execute(sql, parameters) # Query the database

        # Else, only use the sql query
        else:
            result = dbCursor.execute(sql)

        row = result.fetchall() # Store the data

    # Catch Exceptions & return None
    except Exception as e:
        print("select_n_rows failed:", e)
        return None

    # No matter what, close the cursor
    finally:
        if dbCursor is not None:
            dbCursor.close()


    # Get the result, if no results, return []
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

    # Try to connect to database & perform an action
    try:

        # Create a cursor & init data holder
        dbCursor = dbConn.cursor()
        result = None

        # If there are parameters, use them in the .execute
        if (parameters is not None):
            # Query the database
            result = dbCursor.execute(sql, parameters)
        
        # If no parameters, only use the sql query
        else:
            result = dbCursor.execute(sql)

        # Commit the changes to the database
        dbConn.commit()
    
    # Handle any errors & return -1
    except Exception as e:
        print("perform_action failed:", e)
        return -1
    
    # No matter what, close the cursor
    finally:
        dbCursor.close()

    # Return the number of rows modified
    return result.rowcount

    # End perform_action()