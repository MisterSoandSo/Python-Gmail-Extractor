from dotenv import load_dotenv
from backend.backend import credentials, MailList

import os

#Configurations
load_dotenv('.env')
token = os.environ.get("token_path")
secret = os.environ.get("credential_path")
SCOPES = [os.environ.get("scope")]

# GMail API credential generation
# Function will take you Oauth and select the email address yo uwish to use. This will only for the first run.
creds = credentials(secret,token,SCOPES)    

def mainMenu():
    print("~~~~~ Python GMail Terminal Menu ~~~~~")
    print("1. MailList")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Exit")

def mailMenu():
    x = MailList(creds)
    x.print_msgID_Subject(x.get_all_UnreadID())
    x.get_all_UnreadID()
    
def option2():
    pass
def option3():
    pass
def option4():
    pass

def main():
    menu_options = {
        '1': mailMenu,
        '2': option2,
        '3': option3,
        '4': option4,
        '5': exit
    }
    while True:
        mainMenu()
        choice = input("Select >> ")
        if choice in menu_options:
            menu_options[choice]()
        else:
            print("Invalid Input")

if __name__ == '__main__':
    main()