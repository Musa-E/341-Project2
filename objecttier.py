#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through 
# the data tier.
#
# Original author: Ellen Kidane
#
import datatier



##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
class Lobbyist:

   # Constructor
   def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone):
      self._Lobbyist_ID = Lobbyist_ID
      self._First_Name = First_Name
      self._Last_Name = Last_Name
      self._Phone = Phone

   # Properties
   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID
   
   @property
   def First_Name(self):
      return self._First_Name
   
   @property
   def Last_Name(self):
      return self._Last_Name
   
   @property
   def Phone(self):
      return self._Phone

   # End Lobbyist class



##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:

   # Constructor
   def __init__(self, Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, Address_1, Address_2, City, State_Initial,
                Zip_Code, Country, Email, Phone, Fax, Years_Registered, Employers, Total_Compensation):
      self._Lobbyist_ID = Lobbyist_ID
      self._Salutation = Salutation
      self._First_Name = First_Name
      self._Middle_Initial = Middle_Initial
      self._Last_Name = Last_Name
      self._Suffix = Suffix
      self._Address_1 = Address_1
      self._Address_2 = Address_2
      self._City = City
      self._State_Initial = State_Initial
      self._Zip_Code = Zip_Code
      self._Country = Country
      self._Email = Email
      self._Phone = Phone
      self._Fax = Fax
      self._Years_Registered = list(Years_Registered)
      self._Employers = list(Employers)
      self._Total_Compensation = Total_Compensation
   
   # Properties
   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID
   
   @property
   def Salutation(self):
      return self._Salutation

   @property
   def First_Name(self):
      return self._First_Name

   @property
   def Middle_Initial(self):
      return self._Middle_Initial

   @property
   def Last_Name(self):
      return self._Last_Name

   @property
   def Suffix(self):
      return self._Suffix

   @property
   def Address_1(self):
      return self._Address_1

   @property
   def Address_2(self):
      return self._Address_2

   @property
   def City(self):
      return self._City

   @property
   def State_Initial(self):
      return self._State_Initial

   @property
   def Zip_Code(self):
      return self._Zip_Code

   @property
   def Country(self):
      return self._Country

   @property
   def Email(self):
      return self._Email

   @property
   def Phone(self):
      return self._Phone

   @property
   def Fax(self):
      return self._Fax

   @property
   def Years_Registered(self):
      return self._Years_Registered # (List)

   @property
   def Employers(self):
      return self._Employers # (List)

   @property
   def Total_Compensation(self):
      return self._Total_Compensation



##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:

   # Constructor
   def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone, Total_Compensation, Clients):
      self._Lobbyist_ID = Lobbyist_ID
      self._First_Name = First_Name
      self._Last_Name = Last_Name
      self._Phone = Phone
      self._Total_Compensation = Total_Compensation
      self._Clients = Clients

   # Properties
   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID
   
   @property
   def First_Name(self):
      return self._First_Name
   
   @property
   def Last_Name(self):
      return self._Last_Name
   
   @property
   def Phone(self):
      return self._Phone
   
   @property
   def Total_Compensation(self):
      return self._Total_Compensation
   
   @property
   def Clients(self):
      return self._Clients
   
   # End LobbyistClients class



##################################################################
# 
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):

   query = """
      SELECT
         COUNT(DISTINCT LobbyistAndEmployer.Lobbyist_ID) As Lobbyists
      FROM
         LobbyistAndEmployer;
   """

   # Search with the above query
   result = datatier.select_one_row(dbConn, query)

   if (result is not None):

      return result[0]
   else:
      return -1


##################################################################
# 
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
   
   query = """
      SELECT
         COUNT(DISTINCT EmployerInfo.Employer_ID) AS Employers
      FROM
         EmployerInfo
      LEFT JOIN
         LobbyistAndEmployer ON EmployerInfo.Employer_ID = LobbyistAndEmployer.Employer_ID;
   """

   # Search with the above query
   result = datatier.select_one_row(dbConn, query)

   if (result is not None):

      return result[0]
   else:
      return -1

##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
   
   query = """
      SELECT
         COUNT(DISTINCT ClientInfo.Client_ID) As Clients
      FROM
         ClientInfo; 
   """

   # Search with the above query
   result = datatier.select_one_row(dbConn, query)

   if (result is not None):

      return result[0]
   else:
      return -1

##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and % 
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):
   
   query = """
      SELECT DISTINCT
         LobbyistInfo.Lobbyist_ID As Lobbyists,
         LobbyistInfo.First_Name AS FirstNames,
         LobbyistInfo.Last_Name AS LastNames,
         LobbyistInfo.Phone AS PhoneNum
      FROM
         LobbyistInfo
      WHERE
         LobbyistInfo.First_Name LIKE ? OR LobbyistInfo.Last_Name LIKE ?

      ORDER BY
         Lobbyists ASC;
   """

   pattern = ''.join(pattern)
   # Search with the above query
   result = datatier.select_n_rows(dbConn, query, [pattern, pattern])

   if (result is not None):

      Lobbyists = []
      # Iterate through results and store info in object(s)
      for row in result:
         Lobbyist_ID = row[0]
         First_Name = row[1]
         Last_Name = row[2]
         Phone = row[3]

         # Add a new Lobbyist object to the list & Output info
         Lobbyists.append(Lobbyist(Lobbyist_ID, First_Name, Last_Name, Phone))

      # print() # Formatting
      return Lobbyists
   else:
      return [] # Return an empty list
   
   # End get_lobbyists()



##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):

   # Query - Compensation Amount is incorrect (Duplicates from the JOIN statements?)
   query = """
      SELECT
         LobbyistInfo.Lobbyist_ID,
         LobbyistInfo.Salutation,
         LobbyistInfo.First_Name,
         LobbyistInfo.Middle_Initial,
         LobbyistInfo.Last_Name,
         LobbyistInfo.Suffix,
         LobbyistInfo.Address_1,
         LobbyistInfo.Address_2,
         LobbyistInfo.City,
         LobbyistInfo.State_Initial,
         LobbyistInfo.ZipCode,
         LobbyistInfo.Country,
         LobbyistInfo.Email,
         LobbyistInfo.Phone,
         LobbyistInfo.Fax,
         GROUP_CONCAT(DISTINCT LobbyistYears.Year) AS Years_Registered,
         GROUP_CONCAT(DISTINCT EmployerInfo.Employer_Name) AS Employers,
         SUM(Compensation.Compensation_Amount) AS TotalCompensation
      FROM
         LobbyistInfo
      LEFT JOIN
         LobbyistYears ON LobbyistYears.Lobbyist_ID = LobbyistInfo.Lobbyist_ID
      LEFT JOIN
         LobbyistAndEmployer ON LobbyistAndEmployer.Lobbyist_ID = LobbyistInfo.Lobbyist_ID
      LEFT JOIN
         EmployerInfo ON EmployerInfo.Employer_ID = LobbyistAndEmployer.Employer_ID
      JOIN
         Compensation ON Compensation.Lobbyist_ID = LobbyistInfo.Lobbyist_ID
      WHERE
         LobbyistInfo.Lobbyist_ID = ?
      GROUP BY
         LobbyistInfo.Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, LobbyistInfo.Address_1, LobbyistInfo.Address_2, LobbyistInfo.City, LobbyistInfo.State_Initial, LobbyistInfo.ZipCode, LobbyistInfo.Country, LobbyistInfo.Email, LobbyistInfo.Phone, LobbyistInfo.Fax
      ORDER BY
         LobbyistInfo.Lobbyist_ID ASC;
   """

   validIDQuery = """
      SELECT
         LobbyistInfo.First_Name AS NameExists
      FROM
         LobbyistInfo
      WHERE
         LobbyistInfo.Lobbyist_ID = ?;
   """

   lobbyistInfoQuery = """
      SELECT
         LobbyistInfo.Lobbyist_ID,
         LobbyistInfo.Salutation,
         LobbyistInfo.First_Name,
         LobbyistInfo.Middle_Initial,
         LobbyistInfo.Last_Name,
         LobbyistInfo.Suffix,
         LobbyistInfo.Address_1,
         LobbyistInfo.Address_2,
         LobbyistInfo.City,
         LobbyistInfo.State_Initial,
         LobbyistInfo.ZipCode,
         LobbyistInfo.Country,
         LobbyistInfo.Email,
         LobbyistInfo.Phone,
         LobbyistInfo.Fax
      FROM
         LobbyistInfo
      WHERE
         LobbyistInfo.Lobbyist_ID = ?;
   """

   RegisteredYearsQuery = """
      SELECT
         GROUP_CONCAT(DISTINCT LobbyistYears.Year) As Years
      FROM
         LobbyistYears
      WHERE
         LobbyistYears.Lobbyist_ID = ?;
   """

   EmployersQuery = """
      SELECT
         GROUP_CONCAT(DISTINCT EmployerInfo.Employer_Name) As Employers
      FROM
         LobbyistAndEmployer
      JOIN
         EmployerInfo ON LobbyistAndEmployer.Employer_ID = EmployerInfo.Employer_ID
      WHERE
         LobbyistAndEmployer.Lobbyist_ID = ?;
   """

   EmployersQuery = """
      SELECT
         DISTINCT GROUP_CONCAT( EmployerInfo.Employer_Name, "+") As Employers
      FROM
         LobbyistAndEmployer
      JOIN
         EmployerInfo ON LobbyistAndEmployer.Employer_ID = EmployerInfo.Employer_ID
      WHERE
         LobbyistAndEmployer.Lobbyist_ID = ?
      GROUP BY
         EmployerInfo.Employer_Name
      ORDER BY
         EmployerInfo.Employer_Name ASC;
   """

   compenstionQuery = """
      SELECT
         SUM(Compensation_Amount)
      FROM
         Compensation
      WHERE
         Compensation.Lobbyist_ID = ?;
   """

   try:
      idNum = lobbyist_id
      # lobbyist_id = (''.join(lobbyist_id),)
      # Search with the above query 

      # Confirm the ID entered is actually valid
      validID = datatier.select_n_rows(dbConn, validIDQuery, [lobbyist_id])
      
      if (validID == []):  # If an empty list is returned, no match is found
         # print('\033[91m' + '\033[1m' + "No lobbyist with that ID was found.\n" + '\033[0m')
         return None

      lobbyistInfo = datatier.select_n_rows(dbConn, lobbyistInfoQuery, [lobbyist_id])
      RegisteredYearsInfo = datatier.select_one_row(dbConn, RegisteredYearsQuery, [lobbyist_id])
      EmployersInfo = datatier.select_n_rows(dbConn, EmployersQuery, [lobbyist_id])
      compenstionInfo = datatier.select_one_row(dbConn, compenstionQuery, [lobbyist_id])

      # result = datatier.select_n_rows(dbConn, query, lobbyist_id)
      result = lobbyistInfo

      if (result is not None):
         
         # No matches found; return an empty list ---- Needed if the except catches this?
         if (len(result) == 0):
            return None

         tempData = result[0]
         # Convert each element in the tuple to a string
         result = [str(value) for value in tempData]

         # Data extraction (for clarity)
         Lobbyist_ID = result[0]
         Salutation = result[1]
         First_Name = result[2]
         Middle_Initial = result[3]
         Last_Name = result[4]
         Suffix = result[5]
         Address_1 = result[6]
         Address_2 = result[7]
         City = result[8]
         State_Initial = result[9]
         ZipCode = result[10]
         Country = result[11]
         Email = result[12]
         Phone = result[13]
         Fax = result[14]
         Years_Registered = RegisteredYearsInfo[0]
         Employers = EmployersInfo
         TotalCompensation = compenstionInfo[0]
   
         # Split the years based on ',' for output
         Years_Registered = Years_Registered.split(',')

         # Iterate through list of tuple/strings and store vals in a new list (delim = '+')
         tempEmployers = []
         for x in Employers:
            for y in x:
               tempEmployers.extend(y.split('+'))
         
         # Turn into a list, with no duplicates (via set function) and sort
         tempEmployers = list(set(tempEmployers))
         tempEmployers = sorted(tempEmployers)

         # Update Employers with correctly formatted data
         Employers = tempEmployers

         # If a given lobbyist has no listed compensation, set val to 0.00
         if (TotalCompensation is None):
            TotalCompensation = 0.00

         # # Add a new Lobbyist object to the list & Output info
         currLobbyist = LobbyistDetails(Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix,
            Address_1, Address_2, City, State_Initial, ZipCode, Country, Email, Phone, Fax, 
            Years_Registered, Employers, TotalCompensation)

         return currLobbyist
      else:
         return None # Return None
   
   # Handle any exceptions and return None
   except Exception as e:
      # print("get_lobbyist_details failed:", e)
      return None
   
   # End get_lobbyist_details()



##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total 
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid. 
#          An empty list is also returned if an internal error 
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):

   lobbyistInfoQuery = """
      SELECT DISTINCT
         LobbyistInfo.Lobbyist_ID AS ID,
         LobbyistInfo.First_Name AS FirstName,
         LobbyistInfo.Last_Name AS LastName,
         SUM(Compensation.Compensation_Amount) AS Compensation,
         LobbyistInfo.Phone AS PhoneNum,
         GROUP_CONCAT(ClientInfo.Client_Name, '+') AS ClientList
      FROM
         Compensation
      JOIN
         LobbyistInfo ON Compensation.Lobbyist_ID = LobbyistInfo.Lobbyist_ID
      JOIN
         ClientInfo ON Compensation.Client_ID = ClientInfo.Client_ID
      WHERE
         strftime('%Y', Compensation.Period_End) = ?
      GROUP BY
         LobbyistInfo.Lobbyist_ID
      ORDER BY
         Compensation DESC
      LIMIT
         ?;
   """

   try: # Needed?
      # year = (''.join(year),)
      # Search with the above query 

      # Get "N" number of topLobbyists for a given "year"
      topLobbyists = datatier.select_n_rows(dbConn, lobbyistInfoQuery, [year, N])
    # topLobbyistClients = datatier.select_n_rows(dbConn, lobbyistClientsQuery, [year, N])

   except Exception as e: # Needed?
      # print("get_top_N_lobbyists failed:", e)
      return []
   


   # No results; return an empty list
   if (topLobbyists is None):
      # print()
      return []

   else:

      Lobbyists = []
      # Invalid year returned nothing from database; return empty list
      if (len(topLobbyists) == 0):
         return []

      # Iterate through each result (aka lobbyist)
      for i in range(0, N):
         id = topLobbyists[i][0]
         firstName = topLobbyists[i][1]
         lastName = topLobbyists[i][2]
         compensation = topLobbyists[i][3]
         phoneNum = topLobbyists[i][4]
         clients = topLobbyists[i][5]

         # Reconvert/format the clients so that it is in a suitable form
         tempClients = []
         for x in clients.split('+'):
            tempClients.extend(x.split('+'))

         # Turn into a list, with no duplicates (via set function) and sort
         tempClients = list(set(tempClients))
         tempClients = sorted(tempClients)

         # Update clients with correctly formatted data
         clients = tempClients

         if (clients is None):
            clients = []
         
         Lobbyists.append(LobbyistClients(id, firstName, lastName, phoneNum, compensation, clients))

      # Return a list of "lobbyistClients" objects
      return Lobbyists




##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below), 
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):

   # Confirms that the entered lobbyist_id is in the database
   validIDQuery = """
      SELECT
         LobbyistInfo.First_Name AS NameExists
      FROM
         LobbyistInfo
      WHERE
         LobbyistInfo.Lobbyist_ID = ?;
   """

   # Actually updates the database
   insertionQuery = """
      INSERT INTO 
         LobbyistYears (Lobbyist_ID, Year) VALUES ( ? , ? );
   """

   try:
      # Conversion for query
      idNum = lobbyist_id
      lobbyist_id = (''.join(lobbyist_id),)

      # Confirm the ID entered is actually valid
      validID = datatier.select_n_rows(dbConn, validIDQuery, lobbyist_id)

      if (validID == []):  # If no match is found, 0 is returned
         # print('\033[91m' + '\033[1m' + "No lobbyist with that ID was found.\n" + '\033[0m')
         return 0

      # Revert back to original type for the following query
      lobbyist_id = idNum
      insertionResults = datatier.select_n_rows(dbConn, insertionQuery, [lobbyist_id, year])

      if (len(insertionResults) == 0):  # If successfully added, commit to database
         dbConn.commit()
         return 1
      else:
         # print('\033[91m' + '\033[1m' + "FAILED" + '\033[0m')
         return 0

   # Catch any exceptions and return 0
   except Exception as e:
      print("\nadd_lobbyist_year failed:", e)
      return 0

   # End add_lobbyist_year()



##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively 
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):

   # Confirms that the entered lobbyist_id is in the database
   validIDQuery = """
      SELECT
         LobbyistInfo.First_Name AS NameExists
      FROM
         LobbyistInfo
      WHERE
         LobbyistInfo.Lobbyist_ID = ?;
   """

   # Actually updates the database
   updateSalutationQuery = """
      UPDATE 
         LobbyistInfo
      SET 
         Salutation = ?
      WHERE 
         LobbyistInfo.Lobbyist_ID = ? ;
   """

   try:

      idNum = lobbyist_id
      lobbyist_id = (''.join(lobbyist_id),)

      # Confirm the ID entered is actually valid
      validID = datatier.select_n_rows(dbConn, validIDQuery, lobbyist_id)

      if (validID == []):  # If an empty list is returned, no match is found
         # print('\033[91m' + '\033[1m' + "No lobbyist with that ID was found.\n" + '\033[0m')
         return 0
      
      # Revert lobbyist_id and update the database with the new salutation
      lobbyist_id = idNum
      salutationUpdateResults = datatier.select_n_rows(dbConn, updateSalutationQuery, [salutation, lobbyist_id])

      if (len(salutationUpdateResults) == 0): # If successfully added, commit to database

         dbConn.commit()
         return 1
      else:
         # print("set_salutation failed")
         return 0
      
   except Exception as e:
      print("set_salutation failed:", e)
      return 0
   
   # End set_salutation()



# Temp Function that is used during testing; deletes a year/lobbyist entry
# This is mainly so I can keep testing the add_year function without changing
# the actual database too much.
def delLobbyYearTEMP(dbConn, lobbyist_id, year):

   # Todo
   print('\033[91m' + '\033[1m' + "--------\nWarning: This Function MUST be removed before submission\n--------" + '\033[0m')
   # For more info on that text, see:
   # https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal

   validIDQuery = """
      SELECT
         LobbyistInfo.First_Name AS NameExists
      FROM
         LobbyistInfo
      WHERE
         LobbyistInfo.Lobbyist_ID = ?;
   """

   deletionQuery = """
      DELETE FROM 
         LobbyistYears
      WHERE
         LobbyistYears.Lobbyist_ID = ?
         AND
         LobbyistYears.Year = ? ;
   """

   idNum = lobbyist_id
   lobbyist_id = (''.join(lobbyist_id),)

   # Confirm the ID entered is actually valid
   validID = datatier.select_n_rows(dbConn, validIDQuery, lobbyist_id)

   if (validID == []):  # If an empty list is returned, no match is found
      print('\033[91m' + '\033[1m' + "No lobbyist with that ID was found.\n" + '\033[0m')
      return 0

   try:

      lobbyist_id = idNum
      deletionResults = datatier.select_n_rows(dbConn, deletionQuery, [lobbyist_id, year])

      if (len(deletionResults) == 0): # If successfully added, commit to database
         # print("\nResults:", deletionResults, "**")
         dbConn.commit()
         print("\n" + '\033[91m' + '\033[1m' + "Lobbyist successfully unregistered.\n" + '\033[0m')
         return 1
      else:
         return 0


   except Exception as e:
      print("\ndelLobbyYearTEMP failed:", e)
      print()
      return 0