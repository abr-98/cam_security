import os
import subprocess
textfile=open("~/home/cam_security_setup/destination.txt","r")
folder=textfile.read()
textfile.close()
location=folder+"/test_capture.py"
subprocess.call(['chmod', '+x', location])
os.chmod(location, 0o777)
os.chmod(location, 0o755)
os.chmod(location, 0o744)
