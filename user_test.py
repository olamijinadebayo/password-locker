import unittest # importing the unittest module
from user import User # Importing the contact class
import pyperclip

class TestUser(unittest.TestCase):


    def setUp(self):
        '''
        setup up method to run before each test cases.
        '''
        self.new_user = User("Olamijin","09037465697") # create contact oblect

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Olamijin")
        self.assertEqual(self.new_user.password,"09037465697")

if __name__ == '__main__':
    unittest.main()
