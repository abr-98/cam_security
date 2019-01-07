from PIL import Image
import datetime
import os,subprocess
from tkinter import messagebox
def display():
    textfile=open("home/cam_security_setup/destination.txt","r")
    folder=textfile.read()
    textfile.close()
    location=folder+"/time.txt"
    textfile=open(location,"r")
    now_time_str=textfile.read()
    textfile.close()
    now_date=datetime.datetime.now().date().strftime ("%d-%m-%y")
    now_date_str=str(now_date)
    name_frame=folder+"/frame-"+now_date_str+"-"+now_time_str+"/"
    message="Please go to "+name_frame+"/ in the installed folder"
    messagebox.showinfo("File location",message )
    #p.wait()
