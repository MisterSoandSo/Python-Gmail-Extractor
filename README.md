# Python Gmail Extractor

This is a demonstration project that allows you to extract data from specific senders in Gmail to process and to store it locally in a directory.

## Project Objectives

- [x] Connect to Gmail via Python and Credentials
- [ ] Create a terminal client interface
- [ ] Parse for specific senders
- [ ] Extract table data and store it in a CSV
- [x] Automate the process to run regularly
- [ ] ...

## Initial Google Cloud Setup

1. Set up a Google Cloud Project with the Gmail API enabled.
2. Configure OAuth consent screen in APIs & Services. Choose user type as "External." Fill in the required "App Name" and "Email." Modify Scopes and Test Users for your specific needs. If you don't plan to use this in production, ensure you add the necessary test users who will use this application.
3. Authorize the Desktop application via APIs & Services > Credentials. Click "Create Credentials" > "OAuth client ID." Choose "Desktop app" as the application type. The "Name" field is used to identify which credential is used on the console. Create and then download "credentials.json" to your working directory.

## Setup .env file

Copy the following into a `.env` file before running this project:
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
