import tkinter as tk
from subprocess import call
textfile=open("home/cam_security_setup/destination.txt","r")
folder=textfile.read()
textfile.close()

def exec_display_frames():
    location="python3 "+folder+"/caller.py"
    exit_code = call(location, shell=True)
    display_frames.config(state="disabled")

def exec_display_screen():
    location="python3 "+folder+"/caller_screens.py.py"
    exit_code = call(location, shell=True)
    display_screens.config(state="disabled")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.title("Control Panel")
root.geometry('450x400')
button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   width=25,
                   pady=10,
                   command=quit)
#button.place(x=90,y=90)
button.pack(pady=15)

display_frames = tk.Button(frame,
                    text="Display Frames",
                    width=25,
                    pady=10,
                    command=exec_display_frames)

display_frames.pack(pady=15)
display_screens= tk.Button(frame,
                    text="Display Screens",
                    width=25,
                    pady=10,
                    command=exec_display_screen)

display_screens.pack(pady=15)
root.mainloop()
