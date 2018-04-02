import unittest # importing the unittest module
from credentials import Credential # Importing the contact class
import pyperclip

class TestCredential(unittest.TestCase):
    def setUp(self):
        '''
        setup up method to run before each test cases.
        '''
        self.new_credential = Credential("pinterest","Olamijin","09037465697") # create contact oblect
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
    def test_delete_credential(self):
        '''
        test to see if a credential can be deleted
        '''
        self.new_credential.save_credential()
        test_credential = Credential("pinterest", "olamijin", "09037465697") # new credentials
        test_credential.save_credential()

        self.new_credential.delete_credential() # delete credential object
        self.assertEqual(len(Credential.credential_list), 1)
    def test_find_password_by_username(self):
        '''
        test to see if we can find a password using the username
        '''
        self.new_credential.save_credential()
        test_credential = Credential("pinterest", "olamijin", "09037465697")
        test_credential.save_credential()
        found_credential = Credential.find_by_username("olamijin")
        self.assertEqual(found_credential.password, test_credential.password)
    def test_credential_exists(self):
        '''
        test to see if we can return a boolean if a credential is not found
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Facebook", "gitu", "1234asdf")
        test_credential.save_credential()
        credential_exists = Credential.credential_exist("gitu")
        self.assertTrue(credential_exists)
    def test_display_all_credentials(self):
        '''
        returns a list of all saved credentials
        '''
        self.assertEqual(Credential.display_credentials(), Credential.credential_list)
if __name__ == '__main__':
    unittest.main()
