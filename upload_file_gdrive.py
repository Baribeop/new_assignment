# Program to upload files to Google Drive using python

# using file path to upload
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)
path = r"C:\Users\HP\Pictures\Camera Roll"
for file_val in os.listdir(path):
 f =  os.path.join(path, file_val)
 file1 = drive.CreateFile({'parents': [{'id' : "1MSBzpjanOUpxRPmqwlPrx0JwJLNuh7mT"}], 'title': file_val})
 file1.SetContentFile(f)
 file1.Upload()
 

#using the file directly to upload
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()           
drive = GoogleDrive(gauth)

g_file = drive.CreateFile({'parents': [{'id' : "1MSBzpjanOUpxRPmqwlPrx0JwJLNuh7mT"}], 'title': 'app.upload.txt'})
g_file.SetContentString("hello world")
g_file.Upload()

# Required files 
## 'client_secrets.json'
##'settings.yaml'
