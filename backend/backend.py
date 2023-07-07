import base64
import os.path

from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


def credentials(credential, token, SCOPES):
    creds = None
    # Check Credentials
    if os.path.exists(token):
        creds = Credentials.from_authorized_user_file(token, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credential, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token, 'w') as token:
            token.write(creds.to_json())
    
    return creds


def write_email_to_text_file(email_id, body_content):
    file_path = "emails/"+ str(email_id)+ ".txt"  # Specify the file path
    with open(file_path, "w", encoding="utf-8") as file:
        # Write the string to the file
        file.write(body_content)


class EmailMessage():
    def __init__(self,creds,email_id) -> None:
        self.service = build('gmail', 'v1', credentials=creds)
        self.message = self.service.users().messages().get(userId='me',  id=email_id, format='full').execute()
        self.email_id = email_id

    def debugprint_Message(self):
        print(self.message) 

    def get_Subject(self) -> str:
        headers = self.message['payload']['headers']
        return [header['value'] for header in headers if header['name'] == 'Subject'][0]

    def get_Sender(self) -> str:
        headers = self.message['payload']['headers']
        return [header['value'] for header in headers if header['name'] == 'From'][0]

    def get_Date(self):
        headers = self.message['payload']['headers']
        return [header['value'] for header in headers if header['name'] == 'Date'][0]
    
    def get_Body(self):
        parts = self.message['payload']['parts']
        # Recursive function to decode parts
        def decode_parts(parts):
            content = ""
            for part in parts:
                if 'parts' in part:
                    # If part has nested parts, recursively decode them
                    content += decode_parts(part['parts'])
                if 'body' in part and 'data' in part['body']:
                    # Decode the part's data and append to content
                    data = part['body']['data']
                    decoded_data = base64.urlsafe_b64decode(data).decode()
                    content += decoded_data
            return content
        return decode_parts(parts)
    
    def mark_Read(self) -> None:
        self.service.users().messages().modify(userId='me', id=self.email_id, body={'removeLabelIds': ['UNREAD']}).execute()
