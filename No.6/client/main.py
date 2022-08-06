from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload
from urllib.error import HTTPError
from regex import W
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())


    try:
        service = build('drive', 'v3', credentials=creds)
        file_metadata = {'name': 'sample.mp4'}
        media = MediaFileUpload('sample.mp4', mimetype='video/mp4')
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    except HTTPError as error:
        print(F'An error occurred: {error}')
        file = None
    return file.get('id')

if __name__ == '__main__':
    main()