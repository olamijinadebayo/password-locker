#!/usr/bin/env python3.6
from user import User
from credentials import Credential
import uuid

def create_user(ulogin,upword):
    '''
    function to create user account
    '''
    new_user = User(ulogin,upword)
    return new_user

def save_user(acct):
    '''
    save new user account
    '''
    acct.save_user()

def generate_password():
    '''
    function to generate a new password
    '''
    gen_password = User.create_password(string_length=10)
    return gen_password

def auth_user(name, password):
    '''
    function to authenticate a user
    '''
    user_exist = User.user_exist(name, password)
    return user_exist
def create_credential(account, uname, password):
    '''
    function to create a new credential
    '''
    new_cred = Credential(account, uname, password)
    return new_cred

def save_credentials(credential):
    '''
    function to create a new credential
    '''
    credential.save_credential()

def del_credential(credential):
    '''
    function to delete a credential
    '''
    credential.delete_credential()

def find_credential(uname):
    '''
    function that finds a credential by the username and returns it
    '''
    return Credential.find_by_username(uname)
def display_credentials():
    '''
    function that returns all the saved credential
    '''
    return Credential.display_credentials()

def main():
    print("Hello, welcome to Password Locker.")
    print("-" *50)

    while True:
        print("Type 'new' to create and account or 'login' to log in to an existing account.")
        code = input().lower()

        if code == "new":
            print("User name....")
            user_name = input()
            print('\n')

            print("Options: Create your password - 'create'; get generated password - 'gen'")
            option = input()
            while True:
                if option == "create":
                    print("Password....")
                    password = input()
                    break
                elif option == "gen":
                    password = generate_password()
                    print('\n')
                    break
                else:
                    print("Not recognized. Please use one of the codes.")
                    break

            save_user(create_user(user_name, password))
            print(f"Account created successfully. User name: {user_name}, password: {password}. You are currently logged in.")
            print('\n')
            break

        elif code == "login":
            print("Log In")
            print("-"*30)

            print("User name....")
            user_name = input()
            print('\n')

            print("Account password....")
            password = input()
            print('\n')

            sign_in = auth_user(user_name, password)

            if sign_in == True:
                break
            print("Username or password not recognized. Please try again.")
            print('\n')

        else:
            print('\n')
            print("Not recognized. Please use one of the codes.")
            print('\n')


    while True:
            print(f"Please use the following codes to navigate: 'add' - add new credentials, 'list' - show all stored credentials, 'find' - find specific credentials, 'exit' - leave.")

            short_code = input().lower()

            if short_code == 'add':
                    print("New Credentials")
                    print("-" *10)

                    print("To which website does this account belong?")
                    account = input()

                    print("Username....")
                    uname = input()

                    print("Password....")
                    password = generate_password()

                    save_credentials(create_credential(account, uname, password)) #create and save new cred
                    print('\n')
                    print(f"New Credential created: {account}: {uname} -- {password}")
                    print('\n')

            elif short_code == 'list':
                    if display_credentials():
                            print("Here is a list of all your credentials:")
                            print('\n')

                            for credential in display_credentials():
                                    print(f"{credential.account}: {credential.user_name} -- {credential.password}")
                            print('\n')
                    else:
                            print('\n')
                            print("You do not have any credentials saved yet.")
                            print('\n')

            elif short_code == 'find':
                    print("Enter the user name you want to search for.")

                    search_name = input()
                    if find_credential(search_name):
                            search_credential = find_credential(search_name)
                            print('\n')
                            print(f"{credential.website}: {search_credential.user_name} -- {search_credential.password}")
                            print('\n')
                    else:
                        print('\n')
                        print("That credential cannot be found. Please check your spelling and try again.")
                        print('\n')

            elif short_code == 'exit':
                    print("Goodbye...")
                    break
            else:
                print('\n')
                print("Not recognized. Please use one of the short codes.")
                print('\n')

if __name__ == '__main__':
    main()
