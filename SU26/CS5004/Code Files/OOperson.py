class Person: # a structure that represents a person
    """
    This class represents a person. A person has the following attributes: first name, last name, year of birth.
    """
    def __init__(self,firstName,lastName,yearOfBirth): #to instantiate a person
        self.firstName = firstName
        self.lastName = lastName
        self.yearOfBirth = yearOfBirth
    
    def getFirstName(self): 
        """ function for a person to return their first name """
        return self.firstName        
    
    def getLastName(self): 
        """ function for a person to return their last name """
        return self.lastName

    def getYearOfBirth(self): 
        """ function for a person to return their year of birth """
        return self.yearOfBirth

    def getAge(self):
        """ function for a person to return their age in 2020 """
        return 2020 - self.yearOfBirth
 
    def getFullName(self):
        """ function for a person to return their full name """
        return self.firstName + ' ' + self.lastName
        
#create an instance that represents a person named John Doe        
john = Person("John", "Doe", 1945)

########################## Tests ######################

#tests for persons defined in an OO manner

import unittest

class OOPersonTests(unittest.TestCase):
    def setUp(self):
        #create an instance that represents a person named John Doe
        self.john = Person("John", "Doe", 1945)
 
        #create an instance of sally ride
        self.sally = createPerson("Sally", "Ride", 1951)
 
    def test_age(self):
        self.assertEquals(75, self.john.getAge())
        self.assertEquals(69, self.sally.getAge())
 
    def test_fullname(self):
        self.assertEquals("John Doe", self.john.getFullName())
        self.assertEquals("Sally Ride", self.sally.getFullName())
        
suite = unittest.TestLoader().loadTestsFromTestCase(OOPersonTests)
unittest.TextTestRunner(verbosity=2).run(suite)
