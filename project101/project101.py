import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def uploadfiles(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        file_1=open(file_from,'wb')
        dbx.files_upload(file_1.write(),file_to)

def themain():
    access_token='sl.A_5-CkBK2vxxf8nY0Nh24syplrJKtyypRBtopurbFSCz2863KfTA-sTyjDEDgevufYAW3d5il3-lOcx48YhvjeyQyp9Hauy4muVPBizswU0O5fHASOxbJksPkVy50YKfEgNH2iI'
    file_from="C:/Users/saumy/OneDrive/Desktop/project101/dropbox.upload"
    file_to="/project101/dropbox.upload"
    backup=TransferData(access_token)
    backup.uploadfiles(file_from,file_to)
    print("file uploded sucess fully")
    

themain()






















