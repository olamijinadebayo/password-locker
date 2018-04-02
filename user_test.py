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

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user_list array
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)

    def test_user_exists(self):
        '''
        test to see if we can return a boolean if a user is not found
        '''
        self.new_user.save_user()
        test_user = User("Olamijin","09037465697")
        test_user.save_user()
        user_exists = User.user_exist("Olamijin","09037465697")
        self.assertTrue(user_exists)
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

if __name__ == '__main__':
    unittest.main()
