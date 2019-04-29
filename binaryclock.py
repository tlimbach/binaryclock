import turtle
import datetime


def drawBlock(x, y, color):
    width = 1000 / 6 - 20
    height = 1000 / 4 - 20
    corner = width / 4
    flitzi.penup()
    flitzi.color(color)
    flitzi.goto(x + corner, y)
    flitzi.pendown()
    flitzi.begin_fill()
    flitzi.goto(x + width - corner, y)
    flitzi.circle(corner, 90)
    flitzi.goto(x + width, y + height - corner)
    flitzi.circle(corner, 90)
    flitzi.goto(x + corner, y + height)
    flitzi.circle(corner, 90)
    flitzi.goto(x, y + corner)
    flitzi.circle(corner, 90)
    flitzi.end_fill()


def drawtime():
    time = datetime.datetime.now().strftime("%H%M%S")
    for pos in range(6):
        drawDigit(time[pos], pos)

    playground.ontimer(drawtime, 200)


def drawDigit(digit, pos):
    letter = int(digit)

    for row in range(4):
        val = 2 ** (3 - row)
        color = '#111'
        if letter >= val:
            letter = letter - val
            color = 'red'

        key = str(row) + str(pos)

        oldCol = 'white'
        if key in colorMap:
            oldCol = colorMap[key]

        if (oldCol != color):
            drawBlock(pos * (1000 / 6), row * (1000 / 4), color)

        colorMap[key] = color


colorMap = {}

playground = turtle.Screen()
playground.setup(width=500, height=500, startx=None, starty=None)
playground.setworldcoordinates(0, 1000, 1000, 0)
playground.clear()
playground.bgcolor('black')
playground.delay(0)

flitzi = turtle.RawTurtle(playground)
flitzi.hideturtle()
flitzi.speed(0)

drawtime()

playground.exitonclick()