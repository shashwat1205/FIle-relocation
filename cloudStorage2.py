import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def uploadFile(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)
        for root, dirs, files in os.walk(fileFrom):
            for filename in files:
                localPath = os.path.join(root, filename)
                relativePath = os.path.relpath(localPath, fileFrom)
                dropboxPath = os.path.join(fileTo, relativePath)
                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    accessToken = 'sl.BG7j2AJw1XuG5d92grFe0mLpmDR2pj4am0w8qe-7bdXhecQU0YPv1x-on99xcI0P8Qfvru07CVzGOYZ6gC2avvWYfUPUqoMSiF3ky5cuV7HyZhtJ4dELwCoADu0wI3icw8bzJss'
    transferData = TransferData(accessToken)
    fileFrom = str(input("Enter the folder path which you want to transfer"))
    fileTo = input("Enter the path to upload to dropbox ")
    transferData.uploadFile(fileFrom, fileTo)
    print("File has been transferred to your place")

main()