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
