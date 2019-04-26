import turtle
import datetime

colorMap = {}

playground = turtle.Screen()
playground.setup(width=500, height=500, startx=None, starty=None)
playground.setworldcoordinates(0, 1000, 1000, 0)
playground.clear()
playground.bgcolor('black')
playground.delay(0)


def drawBlock(x, y, color):
    flitzi = turtle.RawTurtle(playground)
    flitzi.penup()
    flitzi.hideturtle()
    flitzi.speed(0)
    flitzi.color(color, color)
    flitzi.begin_fill()
    offset = 20
    flitzi.goto(x, y)
    flitzi.pendown()
    flitzi.goto(x + (1000 / 6) - offset, y)
    flitzi.goto(x + (1000 / 6) - offset, y + (1000 / 4) - offset)
    flitzi.goto(x, y + (1000 / 4) - offset)
    flitzi.goto(x, y)
    flitzi.end_fill()


def walk():
    now = datetime.datetime.now()

    hour = ( "0" + str(now.hour))[-2:]
    minute = ( "0" + str(now.minute))[-2:]
    second = ( "0" + str(now.second))[-2:]

    time = hour + minute + second

    drawtime(time)

    playground.ontimer(walk, 900)


def drawtime(time):
    print(time)
    pos = 0
    for d in time:
        pos = pos + 1
        drawDigit(d, pos)


def drawDigit(digit, pos):
    letter = int(digit)

    for row in range(4):
        val = 2 ** (3 - row)
        color = '#111'
        if letter >= val:
            letter = letter - val
            color = 'red'

        key = str(row) + str(pos)

        old_col = 'white'
        if key in colorMap:
            old_col = colorMap[key]

        if old_col != color:
            drawBlock((pos - 1)*(1000 / 6), row*(1000 / 4), color)

        colorMap[key] = color


walk()