import turtle

wn = turtle.Screen()
wn.title('Pong Game')
wn.bgcolor("azure4")
wn.setup(width=800 , height=600)
wn.tracer(0)

#Score
score_1 = 0
score_2 = 0

# Paddle 1
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5 ,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle 2
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5 ,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("DarkOrange4")
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy = 0.3

# Score Table
Score_table = turtle.Turtle()
Score_table.speed(0)
Score_table.color("White")
Score_table.penup()
Score_table.hideturtle()
Score_table.goto(0,270)
Score_table.write("Player_1 : 0 Player_2 : 0", align="center",font=("Courier", 18 ,"italic"))

# Paddle moving functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
    paddle_b.sety(y)
#Keyboard binding
wn.listen()

turtle.onkeypress(paddle_a_up, "w")
turtle.onkeypress(paddle_a_down, "s")

turtle.onkeypress(paddle_b_up, "Up")
turtle.onkeypress(paddle_b_down, "Down")


#Main game loop

while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_1 +=1
        Score_table.clear()
        Score_table.write("Player_1 : {} Player_2 : {}".format(score_1, score_2), align="center", font=("Courier", 18, "italic"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 +=1
        Score_table.clear()
        Score_table.write("Player_1 : {} Player_2 : {}".format(score_1, score_2), align="center",font=("Courier", 18, "italic"))

    #Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.dx *=-1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.dx *=-1
        
        
    
    
    
    #quit---