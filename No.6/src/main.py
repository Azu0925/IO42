
from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload
from urllib.error import HTTPError

import os
import datetime
import cv2
import requests


def main():
    base = os.path.dirname(os.path.abspath(__file__))
    file_name = 'test_' + str(datetime.datetime.now()) + '.m4v'
    file_info = os.path.normpath(os.path.join(base, '../video/' + file_name))

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

    DELTA_MAX = 255
    DOT_TH = 20
    MOTION_FACTOR_TH = 0.20
    avg = None

    while True:
        _, frame = cap.read()
        motion_detected = False
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if avg is None:
            avg = gray.copy().astype('float')
            continue

        cv2.accumulateWeighted(gray, avg, 0.6)
        frame_delta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))

        thresh = cv2.threshold(frame_delta, DOT_TH, DELTA_MAX, cv2.THRESH_BINARY)[1]

        motion_factor = thresh.sum() * 1.0 / thresh.size / DELTA_MAX

        if motion_factor > MOTION_FACTOR_TH:
            motion_detected = True
            print("log: motion_detected True")

        if motion_detected == True:
            print("log: recording start")

            # recording
            record(file_info, cv2, cap)

            # upload to Google drive
            url = upload(file_info, file_name)
            print("log: movie upload done")
            notification.discord(url)

        k = cv2.waitKey(1000)
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


def record(file_path, cv2, cap):
    fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    fps = 20.0
    size = (640, 360)
    limit = datetime.datetime.now() + datetime.timedelta(seconds=10)
    writer = cv2.VideoWriter(file_path, fmt, fps, size)

    while True:
        _, frame = cap.read()
        frame = cv2.resize(frame, size)
        writer.write(frame)

        if datetime.datetime.now() >= limit:
            break

    writer.release()

def upload(file_path, file_name):
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
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
        file_metadata = {'name': file_name}
        media = MediaFileUpload(file_path, mimetype='video/mp4')
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    except HTTPError as error:
        print(F'An error occurred: {error}')
        file = None
    return 'https://drive.google.com/file/d/' + str(file.get('id'))

def discord(content):
    URL = "https://discord.com/api/webhooks/1006111410733977650/RvfguKrfU3qgFRUkEt0Rn4mjtUnOuf87tRKbl5-pXEIFmhYUXPONNEzEbLH3LFOxg8nz"
    header = {
        'Content-Type': 'application/json'
    }
    data = {
        'content': content
    }

    return requests.post(URL, headers=header, json=data)

if __name__ == '__main__':
    main()
