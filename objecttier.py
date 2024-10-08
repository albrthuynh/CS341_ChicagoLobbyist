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
   def __init__(self, lobbyID, firstName, lastName, phone):
      self.Lobbyist_ID = lobbyID
      self.First_Name = firstName
      self.Last_Name = lastName
      self.Phone = phone
   
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
   def __init__(self, lobbyistId, salutation, firstName, mInitial, lastName, suffix, adrs1, adrs2, city, stateInitial, zipCode, country, email, phone, fax, yrsRegistered, employers, totalComp):
      self.Lobbyist_ID = lobbyistId
      self.Salutation = salutation
      self.First_Name = firstName
      self.Middle_Initial = mInitial
      self.Last_Name = lastName
      self.Suffix = suffix
      self.Address_1 = adrs1
      self.Address_2 = adrs2
      self.City = city
      self.State_Initial = stateInitial
      self.Zip_Code = zipCode
      self.Country = country
      self.Email = email
      self.Phone = phone
      self.Fax = fax
      self.Years_Registered = yrsRegistered
      self.Employers = employers
      self.Total_Compensation = totalComp

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
   pass

##################################################################
# 
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
   pass

##################################################################
# 
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
   pass

##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
   pass

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
   pass


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
   pass
         

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