import datetime
import sys
import os
import subprocess
from subprocess import call
img_counter=0
textfile=open("home/cam_security_setup/destination.txt","r")
folder=textfile.read()
textfile.close()
location="python3 "+folder+"/permission.py"
exec_code=call(loaction,shell=True)
#t=0
now_date=datetime.datetime.now().date().strftime ("%d-%m-%y")
now_date_str=str(now_date)
now_time=datetime.datetime.now().time().strftime("%X")
now_time_str=str(now_time)
name_frame=folder+"/frame-"+now_date_str+"-"+now_time_str
name_screen=folder+"/screen-"+now_date_str+"-"+now_time_str
os.makedirs(name_frame)
subprocess.call(['chmod', '+x', name_frame])

os.chmod(name_frame, 0o777)
os.chmod(name_frame, 0o755)
os.chmod(name_frame, 0o744)
#os.chmod(name_frame, '+x')
os.makedirs(name_screen)
subprocess.call(['chmod', '+x', name_screen])
os.chmod(name_screen, 0o777)
os.chmod(name_screen, 0o755)
os.chmod(name_screen, 0o744)
#os.chmod(name_screen, '+x')
count=0
location=folder+"/count_screen.txt"
textfile=open(location,"w")
textfile.write('0')
textfile.close()
location=folder+"/time.txt"
textfile=open(location,"w")
textfile.write(now_time_str)
textfile.close()
location=folder+"/count.txt"
textfile=open(location,"w")
textfile.write('0')
textfile.close()
