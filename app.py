#imported turtle module
import turtle 

wind = turtle.Screen()
wind.title("Ping Pong")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)


#Bat1

Bat1 = turtle.Turtle()
Bat1.speed(0)
Bat1.shape("square")
Bat1.color("blue")
Bat1.penup()
Bat1.goto(-350, 0)
Bat1.shapesize(stretch_wid=5, stretch_len=1)

#Bat2

Bat2 = turtle.Turtle()
Bat2.speed(0)
Bat2.shape("square")
Bat2.color("red")
Bat2.penup()
Bat2.goto(350, 0)
Bat2.shapesize(stretch_wid=5, stretch_len=1)

#Ball

Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.1
Ball.dy = 0.1


#Score

score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0    Player 2: 0", align="center", font=("Courier", 24, "bold"))



#Functions

def Bat1_up():
    y = Bat1.ycor()
    y += 20
    Bat1.sety(y)

def Bat1_down():
    y = Bat1.ycor()
    y -= 20
    Bat1.sety(y)

def Bat2_up():
    y = Bat2.ycor()
    y += 20
    Bat2.sety(y)

def Bat2_down():
    y = Bat2.ycor()
    y -= 20
    Bat2.sety(y)



#Keybinds
    
wind.listen()
wind.onkeypress(Bat1_up, "w")
wind.onkeypress(Bat1_down, "s")
wind.onkeypress(Bat2_up, "Up")
wind.onkeypress(Bat2_down, "Down")




#Game loop
while True:
    wind.update()

    #Move the ball

    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    #Border Check

    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1
    
    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score1 += 1
        score.clear()

        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "bold"))

    
    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "bold"))


    #Bat hits the ball
    
    if (Ball.xcor() > 340 and Ball.xcor() < 350) and (Ball.ycor() < Bat2.ycor() + 40 and Ball.ycor() > Bat2.ycor() - 40):
        Ball.setx(340)
        Ball.dx *= -1
    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (Ball.ycor() < Bat1.ycor() + 40 and Ball.ycor() > Bat1.ycor() - 40):
        Ball.setx(-340)
        Ball.dx *= -1
