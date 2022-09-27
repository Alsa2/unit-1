from library import *
from getpass import getpass

username = input("Username: ")
password = getpass("Password : ")
if simple_login(username, password):
    print("Welcome!")
else:
    print("Wrong username or password!")