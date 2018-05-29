#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:37:17 2018

@author: pt
"""
import pkg_resources
pkg_resources.require("google-api-python-client")
[google-api-python-client 1.5.3 (c:\python27), uritemplate 0.6 (c:\python27\lib\site-packages\uritemplate-0.6-py2.7.egg), six 1.10.0 (c:\python27\lib\site-packages\six-1.10.0-py2.7.egg), oauth2client 3.0.0 (c:\python27\lib\site-packages\oauth2client-3.0.0-py2.7.egg), httplib2 0.9.2 (c:\python27\lib\site-packages\httplib2-0.9.2-py2.7.egg), simplejson 3.8.2 (c:\python27\lib\site-packages\simplejson-3.8.2-py2.7-win32.egg), six 1.10.0 (c:\python27\lib\site-packages\six-1.10.0-py2.7.egg), rsa 3.4.2 (c:\python27\lib\site-packages\rsa-3.4.2-py2.7.egg), pyasn1-modules 0.0.8 (c:\python27\lib\site-packages\pyasn1_modules-0.0.8-py2.7.egg), pyasn1 0.1.9 (c:\python27\lib\site-packages\pyasn1-0.1.9-py2.7.egg)]

from apiclient.discovery import build



from googleapiclient.discovery import build

from googleapiclient.discovery import build
import io, os
from googleapiclient.http import MediaIoBaseDownload
from google.colab import auth

auth.authenticate_user()

drive_service = build('drive', 'v3')
results = drive_service.files().list(
        q="name = 'kaggle.json'", fields="files(id)").execute()
kaggle_api_key = results.get('files', [])

filename = "~/.kaggle/kaggle.json"
os.makedirs(os.path.dirname(filename), exist_ok=True)

request = drive_service.files().get_media(fileId=kaggle_api_key[0]['id'])
fh = io.FileIO(filename, 'wb')
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print("Download %d%%." % int(status.progress() * 100))
os.chmod(filename, 600)