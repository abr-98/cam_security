import os,datetime
def delete():
    textfile=open("~/home/cam_security_setup/destination.txt","r")
    folder=textfile.read()
    textfile.close()
    location=folder+"/time.txt"
    textfile=open(location,"r")
    now_time_str=textfile.read()

    textfile.close()
    now_date=datetime.datetime.now().date().strftime ("%d-%m-%y")
    now_date_str=str(now_date)
    location=folder+"/count_scr.txt"
    textfile=open(location,"r")
    limit=textfile.read()
    i=0
    name_frame=folder+"/frame-"+now_date_str+"-"+now_time_str
    t=int(limit)
    if t==0:
      while i<=t:
        j=str(i)
        img_name=name_frame+"/frame"+j+".jpg"
        #imk=Image.open(img_name)
        #imk.load()
        #imk.show()
        i=i+1
        os.remove(img_name)
    else:
      while i<t:
        j=str(i)
        img_name=name_frame+"/frame"+j+".jpg"
        #imk=Image.open(img_name)
        #imk.load()
        #imk.show()
        i=i+1
        os.remove(img_name)
