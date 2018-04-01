class User():
    """
     class which will generate new instances for every new user
    """
    user_list = []
    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password
