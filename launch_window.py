import tkinter as tk
from subprocess import call
def start():
    """Enable scanning by setting the global flag to True."""
    textfile=open("home/cam_security_setup/destination.txt","r")
    folder=textfile.read()
    textfile.close()
    location="python3 "+folder+"/app_launcher.py"
    exec_code=call(location,shell=True)
    root.destroy()
    location="python3 "+folder+"/window_main.py"
    exec_code=call(location,shell=True)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.title("Control Panel")
root.geometry('350x400')
def sign():
    root.destroy()
    location="python3 "+folder+"/registration_box.py"
    exec_code=call(location,shell=True)

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   width=25,
                   pady=10,
                   command=quit)
    #button.place(x=90,y=90)
button.pack(pady=15)
start = tk.Button(frame,
                  text="Start",
                  width=25,
                  pady=10,
                  command=start)
start.pack(pady=15)

signup = tk.Button(frame,
                  text="Sign Up",
                  width=25,
                  pady=10,
                  command=sign)
signup.pack(pady=55)
label_1 = tk.Label(frame, text="New?? Please register",width=20,font=("bold", 10))
label_1.place(x=30,y=180)
root.mainloop()
