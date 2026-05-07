# create a dictionary that represents a person
def createPerson(firstName,lastName,yearOfBirth):
    """
    This function takes in the various attributes for a person and returns a dictionary with keys for first name, last name and year of birth with their respective values equal to whatever was passed to this function.
    """
    record = {'firstName':firstName, 'lastName':lastName, 'yearOfBirth':yearOfBirth}
    return record

def getAge(person):
    """ function that returns the age of a person """
    return 2020 - person['yearOfBirth']
 
def getFullName(person):
    """ function that returns the full name of a person """
    return person['firstName'] + ' ' + person['lastName']

# create an instance that represents a person named John Doe
john = createPerson("John", "Doe", 1945)

############### tests ###################

# tests for persons defined in a non-OO manner
import unittest

class PersonTests(unittest.TestCase):
    def setUp(self):
        #create an instance that represents a person named John Doe
        self.john = createPerson("John", "Doe", 1945)
 
        #create an instance of sally ride
        self.sally = createPerson("Sally", "Ride", 1951)
 
    def test_age(self):
        self.assertEquals(75, getAge(self.john))
        self.assertEquals(69, getAge(self.sally))
 
    def test_fullname(self):
        self.assertEquals("John Doe", getFullName(self.john))
        self.assertEquals("Sally Ride", getFullName(self.sally))

suite = unittest.TestLoader().loadTestsFromTestCase(PersonTests)
unittest.TextTestRunner(verbosity=2).run(suite)
