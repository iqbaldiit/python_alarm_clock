import db_helper as db
import datetime as dt

class Clock:
    def __init__(self,date_time):
        self.date_time=date_time
    
    
    db_name="db_date_time.csv"
    db_fields=['date_time']
    
    def insert(self):
        return db.insert_update(self.db_name,self.db_fields,{"date_time":self.date_time})

    def get_DateTime(self):
        fileData=db.read(self.db_name)
        abc=[]
        for row in fileData:
            abc.append(''.join([str(r) for r in row]))    
        #fileData=[row for row in fileData if ''.join([str(r) for r in row])>dt.datetime.now().strftime("%d-%m-%Y, %H:%M")]
        return abc

