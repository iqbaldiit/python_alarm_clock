import webbrowser
import db_helper as db
import random

class Youtube_Link:
    def __init__(self,link):
        self.link=link
        pass
    
    
    db_name="db_Links.csv"
    db_fields=['link']
    
    def insert(self):
        return db.insert_update(self.db_name,self.db_fields,{"link":self.link})

    def pick_link(self):
        fileData=db.read(self.db_name)
        return''.join([str(r) for r in random.choice(fileData)])
        #return random.choice(fileData)

    # def redirect_link(link):
    #     return webbrowser.open(link)
