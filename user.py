import uuid
class User():
    """
     class which will generate new instances for every new user
    """
    user_list = []
    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password

    def save_user(self):
        """
        function which will append every instance of the user to the user list
        """
        User.user_list.append(self)
    @classmethod
    def user_exist(cls, name,password):
        '''
        authenticate user if they have an account
        '''
        for user in User.user_list:
            if user.user_name == name and user.password == password:
                return user
        return False

    # def generate_password():
    #     '''
    #     function to generate a new password
    #     '''
    #
    #     alphabet = string.ascii_letters + string.digits
    #     password = ''.join(secrets.choice(alphabet) for i in range(5))
    #
    #     return password

    def random_password(string_length=10):
        """
        Returns a random string of length string_length.
        """
        password = str(uuid.uuid4()) # Convert UUID format to a Python string.
        password = password.upper() # Make all characters uppercase.
        password = password.replace("-","") # Remove the UUID '-'.
        return password[0:string_length] # Return the random string.
