# Python Gmail Extractor
Demo Project. Extract data from specifc senders and store locally in directory.

# Project Objectives
| Tasks                                         | Done |
|-----------------------------------------------|------|
| Connect to Gmail via Python and credentials   | [x]  |
| Create a terminal client interface            | [x]  |
| Parse for specific senders                    | [x]  |
| Extract table data and store in csv           | [x]  |
| Automate process to run regularly             | [x]  |

## Intial Google Cloud Setup
1. Setup a Google Cloud Project with Gmail Api enabled.
2. Setup  OAuth consent screen  in APIs & Services. Choose user type to `External`. Fill in the required `App Name` and `Email`. Modify Scopes and Test Users for your own needs. If you don't plan to push this Production, then make sure to add in the neccessary test users who will be using this application.
3. Authorize Desktop application via APIs & Services > Credentials. Click Create Credentials > OAuth client ID. Click Application type > Desktop app. `Name` field is used to identify which credential is used on console. Create and then download: `credential.json` to your working directory.

## Setup .env file
Copy the following into `.env` before running this project.
```
token_path="filepath/token.json"
credential_path="filepath/credentials.json"
scope="https://www.googleapis.com/auth/gmail.modify"
```

## Usage
```
#Placeholder ... Will be updated on a later date. 
```

## Automation
```
# Windows
In "Task Scheduler", create a new task and set the trigger to run the script with arguements.

# Linux/ Mac
crontab -e
0 8 * * * python main.py option2        #Will run function option2 8am every day

or

0 */2 * * * python main.py option3      #Will run function option3 every 2 hours
```

## Setup Virtual Environment
In the console or terminal, type `python -m venv venv` to initialize the python virtual environment. In linux, you might have to run `sudo apt update && apt update -y` to install pip for later uses.
```
# Windows Users
.\venv\Scripts\activate

# Unix/ Mac Users
source venv/bin/activate

# Exit venv Command
deactivate

```

## Requirements
Using ``pip install -r requirements.txt`` should cover everything.

## License
This project is licensed under the GNU v3 License.