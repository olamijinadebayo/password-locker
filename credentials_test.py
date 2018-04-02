import unittest # importing the unittest module
from credential import Credential # Importing the contact class
import pyperclip

class TestCredential(unittest.TestCase):


    def setUp(self):
        '''
        setup up method to run before each test cases.
        '''
        self.new_credential = Credential("pinterest","Olamijin""09037465697") # create contact oblect

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account,"pinterest")
        self.assertEqual(self.new_credential.user_name,"Olamijin")
        self.assertEqual(self.new_credential.password,"09037465697")

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential_list array
        '''
        self.new_credential.save_credential() # saving the new contact
        self.assertEqual(len(Credential.credential_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []
