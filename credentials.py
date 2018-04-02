
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
