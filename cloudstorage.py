import dropbox 
import os

class TransferData: 
    def __init__(self, access_token): 
        self.access_token = access_token

        f = open(file_from, 'rb') 
        dbx.files_upload(f.read(), file_to) 
        
    def upload_file(self, file_from, file_to): 
        dbx = dropbox.Dropbox(self)
        for root , dirs , files in os.walk(file_from):
            relative_path = os.path.relpath(local_path,file_from)
            dropbox_path = os.path.join(file_to,relative_path)
        with open(local_path,'rb') as f:
            dbx.files.upload(f.read(),dropbox_path,mode-WriteMode('overwrite'))
    def main(): 
        access_token = 'sl.Au3DMho_hVzIUGjeVIqDQd10CK21YMEAclXUzihxm7bFROV9iEPZn5oWBeAz8EOEKN5fHXh_C1pTb6Fj-kieJ3-nePXR4gevBcdaDDb-JB_SdFVWVtl' 
        transferData = TransferData(access_token)

        file_from = input("Enter the file path to transfer : -") 
        file_to = input("enter the full path to upload to dropbox:- ") 

        # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.
         
        # # API v2 
        transferData.upload_file(file_from, file_to) 
        print("File has been moved !!!") 
     
     
    main()