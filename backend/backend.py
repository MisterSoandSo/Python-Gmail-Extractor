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
        

#Handle Extracting information for specifc email ids and marking them as read.
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
        try:
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
        except:
            return "Payload formating Error"
        
    def mark_Read(self) -> None:
        self.service.users().messages().modify(userId='me', id=self.email_id, body={'removeLabelIds': ['UNREAD']}).execute()

    def get_attachments(self):   
        try:
            parts = self.message['payload']['parts']
            # Check if the email has attachments     
        
            for part in parts:
                file_name = part['filename']
                body = part['body']
                
                if 'attachmentId' in body:
                    attachment_id = body['attachmentId']
                    response = self.service.users().messages().attachments().get(userId='me',
                                                                            messageId=self.email_id,
                                                                            id=attachment_id
                                                                            ).execute()
                    file_data = base64.urlsafe_b64decode(response.get('data').encode('UTF-8'))
                    file_path = "emails/"+str(self.email_id)
                    os.makedirs(file_path)
                    with open(file_path+"/"+file_name, 'wb') as _f:
                        _f.write(file_data)
                        print(f'File {file_name} is saved.')
        except:
            pass

    def write_email_to_text_file(self, body_content):
        file_path = "emails/"+ str(self.email_id)+ ".txt"  # Specify the file path
        with open(file_path, "w", encoding="utf-8") as file:
            # Write the string to the file
            file.write(body_content)


# Class handles parsing all Email Ids from email
class MailList():
    def __init__(self,creds) -> None:
        self.service = build('gmail', 'v1', credentials=creds)
        self.creds = creds

    def get_all_UnreadID(self) -> list:
        results = self.service.users().messages().list(userId='me', labelIds=['INBOX'], q='is:unread').execute()
        return results.get('messages', [])
    
    def print_msgID_Subject(self, messages):
        if len(messages) == 0:
            print("No Messages")
            exit()
        else:
            for message in messages:
                print("Message ID: ",message['id'])
                msg = EmailMessage(self.creds,message['id'])
                print("Subject: ",msg.get_Subject())
                print("From: ", msg.get_Sender())
                msg.write_email_to_text_file(msg.get_Body())
                msg.get_attachments()
                print("-"*45)
                
        
    