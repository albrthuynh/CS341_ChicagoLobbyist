#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through 
# the data tier.
#
# Original author: Ellen Kidane
#  * Course: CS 341, Fall 2024
#  * System: MacOS using VSCode
#  * Student Author: Albert Huynh
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
   # constructor for the object
   def __init__(self, lobbyID, firstName, lastName, phone):
      self._Lobbyist_ID = lobbyID
      self._First_Name = firstName
      self._Last_Name = lastName
      self._Phone = phone
   
   # list of properties to get access to these variables because they are private 
   # (getter functions)
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
   # constructor for the details of a lobbyist
   def __init__(self, lobbyistId, salutation, firstName, mInitial, lastName, suffix, adrs1, adrs2, city, stateInitial, zipCode, country, email, phone, fax, yrsRegistered, employers, totalComp):
      self._Lobbyist_ID = lobbyistId
      self._Salutation = salutation
      self._First_Name = firstName
      self._Middle_Initial = mInitial
      self._Last_Name = lastName
      self._Suffix = suffix
      self._Address_1 = adrs1
      self._Address_2 = adrs2
      self._City = city
      self._State_Initial = stateInitial
      self._Zip_Code = zipCode
      self._Country = country
      self._Email = email
      self._Phone = phone
      self._Fax = fax
      self._Years_Registered = yrsRegistered
      self._Employers = employers
      self._Total_Compensation = totalComp

   # list of properties to get access to these variables because they are private 
   # (getter functions)
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
      return self._Years_Registered
   
   @property 
   def Employers(self):
      return self._Employers
   
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
   # constructor for the clients of lobbyists
   def __init__(self, lobbyID, firstName, lastName, phone, totalComp, clients):
      self.Lobbyist_ID = lobbyID
      self.First_Name = firstName
      self.Last_Name = lastName
      self.Phone = phone
      self.Total_Compensation = totalComp
      self.Clients = clients
   
   # list of properties to get access to these variables because they are private 
   # (getter functions)
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

##################################################################
# 
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
   sql = """
      SELECT COUNT(Lobbyist_ID)
      FROM LobbyistInfo
   """

   try:
      row = datatier.select_one_row(dbConn, sql)
      return row[0]
   except Exception as err:
      return -1

##################################################################
# 
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
   sql = """
      SELECT COUNT(Employer_ID)
      FROM EmployerInfo
   """

   try:
      row = datatier.select_one_row(dbConn, sql)
      return row[0]
   except Exception as err:
      return -1

##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
   sql = """
      SELECT COUNT(Client_ID)
      FROM ClientInfo
   """

   try:
      row = datatier.select_one_row(dbConn, sql)
      return row[0]
   except Exception as err:
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
   res = []

   sql = """
      SELECT Lobbyist_ID, First_Name, Last_Name, Phone
      FROM LobbyistInfo
      WHERE First_Name LIKE ? 
      OR Last_Name LIKE ?
      ORDER BY Lobbyist_ID ASC
   """

   rows = datatier.select_n_rows(dbConn, sql, [pattern, pattern])
   
   if len(rows) != 0:
      for row in rows:
         res.append(Lobbyist(row[0], row[1], row[2], row[3]))
   return res
      


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
   getLobbyistInfo = """
      SELECT *
      FROM LobbyistInfo 
      WHERE Lobbyist_ID = ?
   """

   getYearsRegisterd = """
      SELECT Year
      FROM LobbyistYears
      WHERE Lobbyist_ID = ?
   """

   getLobbyistCompensation = """
      SELECT SUM(Compensation_Amount)
      FROM Compensation
      WHERE Lobbyist_ID = ?
   """

   getLobbyistEmployers = """
      SELECT DISTINCT Employer_Name
      FROM EmployerInfo
      JOIN LobbyistAndEmployer
      ON EmployerInfo.Employer_ID = LobbyistAndEmployer.Employer_ID
      WHERE Lobbyist_ID = ?
      ORDER BY Employer_Name 
   """

   lobbyistInfo = datatier.select_one_row(dbConn, getLobbyistInfo, [lobbyist_id])
   yearsRegistered = datatier.select_n_rows(dbConn, getYearsRegisterd, [lobbyist_id])
   lobbyistCompensation = datatier.select_one_row(dbConn, getLobbyistCompensation, [lobbyist_id])
   lobbyistEmployers = datatier.select_n_rows(dbConn, getLobbyistEmployers, [lobbyist_id])

   yearsRegisteredList = []
   lobbyistEmployersList = []
   totalComp = 0

   for row in yearsRegistered:
      yearsRegisteredList.append(row[0])
   
   for row in lobbyistEmployers:
      lobbyistEmployersList.append(row[0])

   if lobbyistCompensation and lobbyistCompensation[0] is not None:
      totalComp = lobbyistCompensation[0]
   

   if lobbyistInfo:
      return LobbyistDetails(lobbyistInfo[0], lobbyistInfo[1], lobbyistInfo[2], lobbyistInfo[3],
      lobbyistInfo[4], lobbyistInfo[5], lobbyistInfo[6], lobbyistInfo[7], lobbyistInfo[8], lobbyistInfo[9],
      lobbyistInfo[10], lobbyistInfo[11], lobbyistInfo[12], lobbyistInfo[13], lobbyistInfo[14],
      yearsRegisteredList, lobbyistEmployersList, totalComp)
   return None

         

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