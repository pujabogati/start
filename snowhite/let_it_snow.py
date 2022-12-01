from random import randint
import turtle
import numpy as np
import pygetwindow
import pyautogui
import PIL.ImageGrab
from PIL import Image


def main(speed=0, bg_color="grey"):
    # create Turtle object
    turtle_screen = turtle.Screen()
    myTurtle = turtle.Turtle()
    
    # set speed to 'fastest = 0'
    turtle.colormode(255)
    myTurtle.speed(speed)
    # change background color
    turtle_screen.bgcolor(bg_color)


    """TODO: define different colors here"""

    for _ in range(10):
        # define some params
        size = 18
        pos = [np.random.randint(-300, 300), np.random.randint(-300, 300)]

        """TODO: set snowflake color here (one of the colors defined above)"""

        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)

        # Go to the start position of the snowflake
        myTurtle.penup()
        myTurtle.goto(pos[0], pos[1])
        myTurtle.pendown()
        myTurtle.color((r,g,b))

        # draw the snowflake
        for _ in range(8):
            snowflake_branch(size, myTurtle)
            myTurtle.left(45)

    path = '.\image.png'
    win = pygetwindow.getWindowsWithTitle('Python Turtle Graphics')[0]
    left, top = win.topleft
    right, bottom = win.bottomright
    pyautogui.screenshot(path)
    im = Image.open(path)
    im = im.crop((left+10, top, right-10, bottom-10))
    im.save(path)
    im.show(path)
    turtle.Screen().exitonclick()


def snowflake_branch(size, myTurtle):
    # This function draws one branch of the snowflake.
    for _ in range(3):
        for _ in range(3):
            myTurtle.forward(size / 3)
            myTurtle.backward(size / 3)
            myTurtle.right(45)
        myTurtle.left(90)
        myTurtle.backward(size / 3)
        myTurtle.left(45)
    myTurtle.right(90)
    myTurtle.forward(size)

if __name__ == "__main__":
    main()

