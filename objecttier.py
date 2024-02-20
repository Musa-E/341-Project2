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
      
      print("\nNumber of lobbyists found:", len(result), "\n")

      # If there are more than 100 matches, display error message and prompt user to narrow search
      if (len(result) > 100):
         print("There are too many lobbyists to display, please narrow your search and try again...\n")
         return []
      
      # No matches found; return an empty list
      if (len(result) == 0):
         return []

      Lobbyists = []
      # Iterate through results and store info in object(s)
      for row in result:
         Lobbyist_ID = row[0]
         First_Name = row[1]
         Last_Name = row[2]
         Phone = row[3]

         # Add a new Lobbyist object to the list & Output info
         Lobbyists.append(Lobbyist(Lobbyist_ID, First_Name, Last_Name, Phone))
         print(Lobbyist_ID, ": " + First_Name, Last_Name + " Phone:", Phone)

      print() # Formatting
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
      lobbyist_id = (''.join(lobbyist_id),)
      # Search with the above query 

      # Confirm the ID entered is actually valid
      validID = datatier.select_n_rows(dbConn, validIDQuery, lobbyist_id)
      
      if (validID == []):  # If an empty list is returned, no match is found
         print("No lobbyist with that ID was found.\n")
         return None

      lobbyistInfo = datatier.select_n_rows(dbConn, lobbyistInfoQuery, lobbyist_id)
      RegisteredYearsInfo = datatier.select_one_row(dbConn, RegisteredYearsQuery, lobbyist_id)
      EmployersInfo = datatier.select_n_rows(dbConn, EmployersQuery, lobbyist_id)
      compenstionInfo = datatier.select_one_row(dbConn, compenstionQuery, lobbyist_id)

      # result = datatier.select_n_rows(dbConn, query, lobbyist_id)
      result = lobbyistInfo

      if (result is not None):
         
         # No matches found; return an empty list
         if (len(result) == 0):
            return None
         
         print(idNum, ":")

         # Lobbyists = [] # Store a list of lobbyist details

         tempData = result[0]
         # Convert each element in the tuple to a string
         result = [str(value) for value in tempData]

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
         
         print("  Full Name: " + First_Name, Middle_Initial, Last_Name)
         print("  Address: " + Address_1 + ", " + City + " , " + State_Initial, ZipCode,", " + Country)
         print("  Email: " + Email)
         print("  Phone: " + Phone)
         print("  Fax: " + Fax)
         print("  Years Registered:", end=' ')
   
         Years_Registered = Years_Registered.split(',')

         for i in range(0, len(Years_Registered)):
            print(Years_Registered[i], end=', ')

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

         # Display
         print("\n  Employers:", end=' ')
         for i in range(0, len(Employers)):
            print(f"{Employers[i]}", end=", ")

         # If a given lobbyist has no listed compensation, set val to 0.00
         if (TotalCompensation is None):
            TotalCompensation = 0.00

         print() # Formatting
         print(f"  Total Compensation: ${TotalCompensation:,.2f}")

         # # Add a new Lobbyist object to the list & Output info
         currLobbyist = LobbyistDetails(Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix,
            Address_1, Address_2, City, State_Initial, ZipCode, Country, Email, Phone, Fax, 
            Years_Registered, Employers, TotalCompensation)
         
         
         # Lobbyists.append(currLobbyist)

         print() # Formatting
         return currLobbyist
      else:
         return [] # Return an empty list
      
   except Exception as e:
      print("get_lobbyist_details failed:", e)
      return []
   
   # End get_lobbyists()



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

   # Invalid N value; return an empty list
   if (N <= 0):
      print("Please enter a positive value for N...")
      return []
   
   lobbyistInfoQuery = """
      SELECT
         LobbyistInfo.First_Name AS FirstName,
         LobbyistInfo.Last_Name AS LastName,
         SUM(Compensation.Compensation_Amount) AS TotalCompensation,
         LobbyistInfo.Phone AS PhoneNum,
         LobbyistYears.Year AS currYear
      FROM
         LobbyistInfo
      JOIN
         Compensation ON Compensation.Lobbyist_ID = LobbyistInfo.Lobbyist_ID
      JOIN
         LobbyistYears ON LobbyistYears.Lobbyist_ID = LobbyistInfo.Lobbyist_ID
      WHERE
         LobbyistYears.Year = ?
      GROUP BY
         LobbyistInfo.Lobbyist_ID, LobbyistInfo.First_Name, LobbyistInfo.Last_Name, LobbyistInfo.Phone
      ORDER BY
         SUM(Compensation.Compensation_Amount) DESC
      LIMIT
         ?;
   """


   lobbyistClientsQuery = """

   """

   try: # Needed?
      # year = (''.join(year),)
      # Search with the above query 

      # Get "N" number of topLobbyists for a given "year"
      topLobbyists = datatier.select_n_rows(dbConn, lobbyistInfoQuery, [year, N])
    # topLobbyistClients = datatier.select_n_rows(dbConn, lobbyistClientsQuery, [year, N])

   except Exception as e: # Needed?
      print("get_top_N_lobbyists failed:", e)
      return []
   


   # No results; return an empty list
   if (topLobbyists is None):
      print()
      return []

   else:

      # Invalid year returned nothing from database; return empty list
      if (len(topLobbyists) == 0):
         print("\nInvalid Year...\n")
         return []
      
      print("\nTop", N, "Lobbyists for", year, ":\n")

      for i in range(0, N):
         firstName = topLobbyists[i][0]
         lastName = topLobbyists[i][1]
         compensation = topLobbyists[i][2]
         phoneNum = topLobbyists[i][3]
         print(f"{i} .", firstName, lastName)
         print("  Phone Number:", phoneNum)
         print(f"  Compensation: ${compensation:,}")
         
         print()

      print(N, "lobbyists listed:\n")
      print()

   pass


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
   pass


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
   pass