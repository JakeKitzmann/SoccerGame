import turtle
import random
import time

# Score
score_a = 0
score_b = 0

# window
window = turtle.Screen()
window.title("Soccer")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# foul lines
rightFoul = turtle.Turtle()
rightFoul.color("blue")
rightFoul.width(5)
rightFoul.left(180)
rightFoul.penup()
rightFoul.goto(270, -55)
rightFoul.pendown()
for x in range(180):
    rightFoul.forward(1)
    rightFoul.right(1)
rightFoul.hideturtle()
    
leftFoul = turtle.Turtle()
leftFoul.color("orange")
leftFoul.width(5)
leftFoul.penup()
leftFoul.goto(-270, 57)
leftFoul.pendown()
for x in range(180):
    leftFoul.forward(1)
    leftFoul.right(1)
leftFoul.hideturtle()

# foul pen
penF = turtle.Turtle()
penF.speed(0)
penF.shape("square")
penF.color("white")
penF.penup()
penF.hideturtle()
penF.goto(0, 70)

# player A shape
PlayerA = turtle.Turtle()
PlayerA.speed(0)
PlayerA.shape("square")
PlayerA.color("Orange")
PlayerA.shapesize(stretch_wid=3,stretch_len=3)
PlayerA.penup()
PlayerA.goto(-50, 0)

# player B shape
PlayerB = turtle.Turtle()
PlayerB.speed(0)
PlayerB.shape("square")
PlayerB.color("Blue")
PlayerB.shapesize(stretch_wid=3,stretch_len=3)
PlayerB.penup()
PlayerB.goto(50, 0)

# ball shape/dxy
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .4
ball.dy = .4
deciderA = random.random()
deciderB = random.random()
if deciderA > .5:
    ball.dx *= -1
if deciderB > .5:
    ball.dy *= -1

# right goal shape
GoalR = turtle.Turtle()
GoalR.speed(0)
GoalR.shape("square")
GoalR.color("white")
GoalR.shapesize(stretch_wid=7, stretch_len=.5)
GoalR.penup()
GoalR.goto(350, 0)

# left goal shape
GoalL = turtle.Turtle()
GoalL.speed(0)
GoalL.shape("square")
GoalL.color("white")
GoalL.shapesize(stretch_wid=7, stretch_len=.5)
GoalL.penup()
GoalL.goto(-350, 0)

# right top goal post shape
GoalTR = turtle.Turtle()
GoalTR.speed(0)
GoalTR.shape("square")
GoalTR.color("white")
GoalTR.shapesize(stretch_wid=.5, stretch_len=4)
GoalTR.penup()
GoalTR.goto(315, 75)

# right bottom goal post shape
GoalBR = turtle.Turtle()
GoalBR.speed(0)
GoalBR.shape("square")
GoalBR.color("white")
GoalBR.shapesize(stretch_wid=.5, stretch_len=4)
GoalBR.penup()
GoalBR.goto(315, -75)

# left top goal post shape
GoalTL = turtle.Turtle()
GoalTL.speed(0)
GoalTL.shape("square")
GoalTL.color("white")
GoalTL.shapesize(stretch_wid=.5, stretch_len=4)
GoalTL.penup()
GoalTL.goto(-315, 75)

# left bottom goal post shape
GoalBL = turtle.Turtle()
GoalBL.speed(0)
GoalBL.shape("square")
GoalBL.color("white")
GoalBL.shapesize(stretch_wid=.5, stretch_len=4)
GoalBL.penup()
GoalBL.goto(-315, -75)

# player A controls
def PlayerAup():
    y = PlayerA.ycor()
    y += 25
    PlayerA.sety(y)

def PlayerAdown():
    y = PlayerA.ycor()
    y -= 25
    PlayerA.sety(y)

def PlayerAleft():
    x = PlayerA.xcor()
    x -= 25
    PlayerA.setx(x)

def PlayerAright():
    x = PlayerA.xcor()
    x += 25
    PlayerA.setx(x)

window.listen()
window.onkey(PlayerAup, "w")
window.onkey(PlayerAdown, "s")
window.onkey(PlayerAleft, "a")
window.onkey(PlayerAright, "d")

# player B controls
def PlayerBup():
    y = PlayerB.ycor()
    y += 25
    PlayerB.sety(y)

def PlayerBdown():
    y = PlayerB.ycor()
    y -= 25
    PlayerB.sety(y)

def PlayerBleft():
    x = PlayerB.xcor()
    x -= 25
    PlayerB.setx(x)

def PlayerBright():
    x = PlayerB.xcor()
    x += 25
    PlayerB.setx(x)

window.listen()
window.onkey(PlayerBup, "i")
window.onkey(PlayerBdown, "k")
window.onkey(PlayerBleft, "j")
window.onkey(PlayerBright, "l")

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# PenG
penG = turtle.Turtle()
penG.speed(0)
penG.shape("square")
penG.color("white")
penG.penup()
penG.hideturtle()
penG.goto(0, 0)

# main
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # wall collisions
    if ball.ycor() > 290:
        ball.sety(289)
        ball.dy *= -1
    
    elif ball.ycor() < -290:
        ball.sety(-289)
        ball.dy *= -1

    if ball.xcor() > 380:
        ball.setx(379)
        ball.dx *= -1
        
    if ball.xcor() < -380:
        ball.setx(-379)
        ball.dx *= -1

    # player/ball collisions A
    if ball.xcor() < PlayerA.xcor() + 40 and ball.xcor() > PlayerA.xcor() - 40 and ball.ycor() < PlayerA.ycor() + 40\
        and ball.ycor() > PlayerA.ycor() - 40 and ball.ycor() > PlayerA.ycor() + 39:
        ball.dy *= -1

    if ball.xcor() < PlayerA.xcor() + 40 and ball.xcor() > PlayerA.xcor() - 40 and ball.ycor() < PlayerA.ycor() + 40 \
        and ball.ycor() > PlayerA.ycor() - 40 and ball.ycor() < PlayerA.ycor() -39:
        ball.dy *= -1

    if ball.xcor() < PlayerA.xcor() + 40 and ball.xcor() > PlayerA.xcor() - 40 and ball.ycor() < PlayerA.ycor() + 40 \
        and ball.ycor() > PlayerA.ycor() - 40 and ball.xcor() < PlayerA.xcor() -39:
        ball.dx *= -1

    if ball.xcor() < PlayerA.xcor() + 40 and ball.xcor() > PlayerA.xcor() - 40 and ball.ycor() < PlayerA.ycor() + 40 \
        and ball.ycor() > PlayerA.ycor() - 40 and ball.xcor() > PlayerA.xcor() +39:
        ball.dx *= -1

    # player/ball collisions B
    if ball.xcor() < PlayerB.xcor() + 40 and ball.xcor() > PlayerB.xcor() - 40 and ball.ycor() < PlayerB.ycor() + 40 \
        and ball.ycor() > PlayerB.ycor() - 40 and ball.ycor() > PlayerB.ycor() + 39:
        ball.dy *= -1
    if ball.xcor() < PlayerB.xcor() + 40 and ball.xcor() > PlayerB.xcor() - 40 and ball.ycor() < PlayerB.ycor() + 40 \
        and ball.ycor() > PlayerB.ycor() - 40 and ball.ycor() < PlayerB.ycor() - 39:
        ball.dy *= -1
    if ball.xcor() < PlayerB.xcor() + 40 and ball.xcor() > PlayerB.xcor() - 40 and ball.ycor() < PlayerB.ycor() + 40 \
        and ball.ycor() > PlayerB.ycor() - 40 and ball.xcor() > PlayerB.xcor() + 39:
        ball.dx *= -1
    if ball.xcor() < PlayerB.xcor() + 40 and ball.xcor() > PlayerB.xcor() - 40 and ball.ycor() < PlayerB.ycor() + 40 \
        and ball.ycor() > PlayerB.ycor() - 40 and ball.xcor() < PlayerB.xcor() - 39:
        ball.dx *= -1

    
# Player A Foul

    # inside 
    if ball.xcor() < PlayerA.xcor() + 40 and ball.xcor() > PlayerA.xcor() - 40 and ball.ycor() < PlayerA.ycor() + 40 and ball.ycor() > PlayerA.ycor() - 40\
    and PlayerA.ycor() > -35 and PlayerA.ycor() < 35 and PlayerA.xcor() < -190 and PlayerA.xcor() > -350:
        score_b += 1
        penF.write("Foul! 1 point for Player B", align = "center", font = ("Courier", 24, "normal"))
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        penF.clear()
        ball.goto(0, 0)
        ball.dx = .5
        ball.dy = .5
        deciderA = random.random()
        deciderB = random.random()
        if deciderA > .5:
            ball.dx *= -1
        if deciderB > .5:
            ball.dy *= -1

    # outside bottom
    if ball.xcor() < PlayerA.xcor() + 40 and ball.xcor() > PlayerA.xcor() - 40 and ball.ycor() < PlayerA.ycor() + 40 and ball.ycor() > PlayerA.ycor() - 40\
    and PlayerA.ycor() > 65 and PlayerA.ycor() < -35 and PlayerA.xcor() < -210 and PlayerA.xcor() > -350:
        score_b += 1
        penF.write("Foul! 1 point for Player B", align = "center", font = ("Courier", 24, "normal"))
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        penF.clear()
        ball.goto(0, 0)
        ball.dx = .5
        ball.dy = .5
        deciderA = random.random()
        deciderB = random.random()
        if deciderA > .5:
            ball.dx *= -1
        if deciderB > .5:
            ball.dy *= -1

    # outside top
    if ball.xcor() < PlayerA.xcor() + 40 and ball.xcor() > PlayerA.xcor() - 40 and ball.ycor() < PlayerA.ycor() + 40 and ball.ycor() > PlayerA.ycor() - 40\
    and PlayerA.ycor() > 35 and PlayerA.ycor() < 65 and PlayerA.xcor() < -210 and PlayerA.xcor() > -350:
        score_b += 1
        penF.write("Foul! 1 point for Player B", align = "center", font = ("Courier", 24, "normal"))        
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        penF.clear()
        ball.goto(0, 0)
        ball.dx = .5
        ball.dy = .5
        deciderA = random.random()
        deciderB = random.random()
        if deciderA > .5:
            ball.dx *= -1
        if deciderB > .5:
            ball.dy *= -1

# Player B Foul

    # inside 
    if ball.xcor() < PlayerB.xcor() + 40 and ball.xcor() > PlayerB.xcor() - 40 and ball.ycor() < PlayerB.ycor() + 40 and ball.ycor() > PlayerB.ycor() - 40\
    and PlayerB.ycor() > -35 and PlayerB.ycor() < 35 and PlayerB.xcor() > 190 and PlayerB.xcor() < 350:
        score_b += 1
        penF.write("Foul! 1 point for Player A", align = "center", font = ("Courier", 24, "normal"))
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        penF.clear()
        ball.goto(0, 0)
        ball.dx = .5
        ball.dy = .5
        deciderA = random.random()
        deciderB = random.random()
        if deciderA > .5:
            ball.dx *= -1
        if deciderB > .5:
            ball.dy *= -1

    # outside bottom
    if ball.xcor() < PlayerB.xcor() + 40 and ball.xcor() > PlayerB.xcor() - 40 and ball.ycor() < PlayerB.ycor() + 40 and ball.ycor() > PlayerB.ycor() - 40\
    and PlayerB.ycor() > 65 and PlayerB.ycor() < -35 and PlayerB.xcor() > 210 and PlayerB.xcor() < 350:
        score_b += 1
        penF.write("Foul! 1 point for Player A", align = "center", font = ("Courier", 24, "normal"))
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        penF.clear()
        ball.goto(0, 0)
        ball.dx = .5
        ball.dy = .5
        deciderA = random.random()
        deciderB = random.random()
        if deciderA > .5:
            ball.dx *= -1
        if deciderB > .5:
            ball.dy *= -1

    # outside top
    if ball.xcor() < PlayerB.xcor() + 40 and ball.xcor() > PlayerB.xcor() - 40 and ball.ycor() < PlayerB.ycor() + 40 and ball.ycor() > PlayerB.ycor() - 40\
    and PlayerB.ycor() > 35 and PlayerB.ycor() < 65 and PlayerB.xcor() > 210 and PlayerB.xcor() < 350:
        score_b += 1
        penF.write("Foul! 1 point for Player A", align = "center", font = ("Courier", 24, "normal"))
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        time.sleep(3)
        penF.clear()
        ball.goto(0, 0)
        ball.dx = .5
        ball.dy = .5
        deciderA = random.random()
        deciderB = random.random()
        if deciderA > .5:
            ball.dx *= -1
        if deciderB > .5:
            ball.dy *= -1


    # goal/ball collision
    if ball.xcor() < GoalR.xcor() + 10 and ball.xcor() < GoalR.xcor() +9 and ball.xcor() > GoalR.xcor() - 10\
    and ball.ycor() < GoalR.ycor() + 70 and ball.ycor() > GoalR.ycor() - 70:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        penG.write("Player A GOAL!!!", align="center", font =("Courier", 30,"normal"))
        time.sleep(3)
        penG.clear()
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dx = .5
        ball.dy = .5
        deciderA = random.random()
        deciderB = random.random()
        if deciderA > .5:
            ball.dx *= -1
        if deciderB > .5:
            ball.dy *= -1
    if ball.xcor() < GoalR.xcor() + 10 and ball.xcor() > GoalR.xcor() +9 and ball.xcor() > GoalR.xcor() - 10\
    and ball.ycor() < GoalR.ycor() + 70 and ball.ycor() > GoalR.ycor() - 70:
        ball.dx *= -1
    if ball.xcor() > GoalL.xcor() - 10 and ball.xcor() > GoalL.xcor() -9 and ball.xcor() < GoalL.xcor() + 10\
    and ball.ycor() < GoalL.ycor() + 70 and ball.ycor() > GoalL.ycor() - 70:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        penG.write("Player B GOAL!!!", align="center", font =("Courier", 30,"normal"))
        time.sleep(3)
        penG.clear()
        ball.goto(0, 0)
        ball.dx = .5
        ball.dy = .5
        deciderA = random.random()
        deciderB = random.random()
        if deciderA > .5:
            ball.dx *= -1
        if deciderB > .5:
            ball.dy *= -1
    if ball.xcor() > GoalL.xcor() - 10 and ball.xcor() < GoalL.xcor() -9 and ball.xcor() < GoalL.xcor() + 10\
    and ball.ycor() < GoalL.ycor() + 70 and ball.ycor() > GoalL.ycor() - 70:
        ball.dx *= -1

    # goal post collisions
    if ball.xcor() < GoalTR.xcor() + 50 and ball.xcor() > GoalTR.xcor() - 50 and ball.ycor() < GoalTR.ycor() + 10\
    and ball.ycor() > GoalTR.ycor() - 10:
        ball.dy *= -1
    if ball.xcor() < GoalBR.xcor() + 50 and ball.xcor() > GoalBR.xcor() - 50 and ball.ycor() < GoalBR.ycor() + 10\
    and ball.ycor() > GoalBR.ycor() - 10:
        ball.dy *= -1

    if ball.xcor() < GoalTL.xcor() + 50 and ball.xcor() > GoalTL.xcor() - 50 and ball.ycor() < GoalTL.ycor() + 10\
    and ball.ycor() > GoalTL.ycor() - 10:
        ball.dy *= -1
    if ball.xcor() < GoalBL.xcor() + 50 and ball.xcor() > GoalBL.xcor() - 50 and ball.ycor() < GoalBL.ycor() + 10\
    and ball.ycor() > GoalBL.ycor() - 10:
        ball.dy *= -1
        