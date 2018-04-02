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
    account.save_user()

def generate_password():
    '''
    function to generate a new password
    '''
    gen_password = User.create_password()
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
