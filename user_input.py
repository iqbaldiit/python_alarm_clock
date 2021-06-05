
import webbrowser
import db_helper as db
import random
import datetime as dt
import youtube_link as yl
import clock as ck


# Variable declaration
link=""
date_time=""

#Taking user input
intent=int(input("Add Link press 1 \nAdd Date & Time (ex: ""06-06-2021, 11:45"") press 2 \nAlarm press 3: "))

if intent==1:
    link=input("Please input a valid link: ")
elif intent==2:
    date_time=input("Please input a valid date time: ")
else:
    pass


Video_Link=yl.Youtube_Link(link)
Alarm=ck.Clock(date_time)

if intent==1:
    print(Video_Link.insert())

if intent==2:
    print(Alarm.insert())

if intent==3:
    Alarm_Times=Alarm.get_DateTime()
    Alarm_Times.sort()

    for i in Alarm_Times:
        if i==dt.datetime.now().strftime("%d-%m-%Y, %H:%M"):
            webbrowser.open(Video_Link.pick_link())






#print(Video_Link.insert_link())
#link=Video_Link.pick_link()
# print (link)
#webbrowser.open(link)
#link="https://www.youtube.com/watch?v=RsXZOuWAAVM&t=600s"

#print(dt.datetime.now().strftime("%d-%m-%Y, %H:%M"))
# dtime="06-06-2021, 11:45"
# Alarm=ck.Clock(dtime)
# print(Alarm.insert())
#print (dt.datetime.now().strftime("%d-%m-%Y, %H:%M")>cureent_time)
# print (dt.datetime.strptime(cureent_time,"%d-%m-%Y, %H:%M"))
#print (dt.datetime.strptime(dt.datetime.now(),"%d-%m-%Y, %H:%M"))
#print(Alarm_Times)

#print(dt.datetime.strptime('06-06-2021, 11:48',"%d-%m-%Y, %H:%M"))


