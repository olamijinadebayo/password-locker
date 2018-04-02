
class Credential(object):
    """
    docstring for Credential.
    """
    credential_list = []
    def __init__(self,account,user_name,password):
        self.account = account
        self.user_name = user_name
        self.password = password

    def save_credential(self):
        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        remove credential objects from credential list
        '''
        Credential.credential_list.remove(self)

    @classmethod
    def find_by_username(cls, name):
        '''
        method takes in the user name and returns a credential that matches it
        '''
        for credential in cls.credential_list:
            if credential.user_name == name:
                return credential

    @classmethod
    def credential_exist(cls, name):
        for credential in cls.credential_list:
            if credential.user_name == name:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        '''
        returns the credential list
        '''
        return cls.credential_list
