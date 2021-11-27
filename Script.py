import time
import turtle

#VARIABLES
delay = 0.1
highscore = 0
score = 0

#SCREEN
wn = turtle.Screen()
wn.title("SNAKE BY-JOSH")
wn.setup(width=700, height=500)
wn.bgcolor("black")
wn.tracer(0)

#PLAYER
tr = turtle.Turtle()
tr.shape("square")
tr.color("white")
tr.penup()
tr.goto(0, 0)
tr.direction = "stop"

#PEN
pn = turtle.Turtle()
pn.speed(0)
pn.shape("square")
pn.color("white")
pn.hideturtle()
pn.goto(0, 270)
pn.write(f"Score: {score} High-score: {highscore}")

def jump():
    if tr.direction != "up":
        tr.direction = "up"
        y = tr.ycor()
        tr.ycor(x += 10)

def move():
    if tr.direction != "right":
        tr.direction = "right"
        x = tr.xcor()
        tr.xcor(x += 10)


wn.listen()
wn.onkeypress(jump, "w")
wn.onkeypress(move, "d")

while True:
    wn.update()
    
    
    time.sleep(delay)