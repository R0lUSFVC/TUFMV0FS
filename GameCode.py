import turtle 
import time
import random

def runGame():
    screen = turtle.Screen()
    player = turtle.Turtle()
    while True:
        inte = str(random.randint(1118481,16777215))
        inte = str(inte)
        rand = str(hex(int(inte)))
        rand = rand[2:]
        screen.bgcolor(f"#{rand}")
        for i in range(80):
            player.forward(1)
            inte = str(random.randint(1118481,16777215))
            inte = str(inte)
            rand = str(hex(int(inte)))
            rand = rand[2:]
            screen.bgcolor(f"#{rand}")
            
        player.left(90)
        player.forward(100)
        player.right(90)
        player.forward(80)
        player.penup()
        player.right(180)
        player.forward(160)
        player.pendown()
        player.left(90)
        player.forward(50)
        player.left(90)
        player.forward(160)
        player.right(90)
        player.forward(50)
    screen.mainloop()