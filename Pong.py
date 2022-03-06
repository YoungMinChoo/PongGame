import turtle as t


# Movement
def leftplayerup():
    y = leftPaddle.ycor()
    y = y + 40
    leftPaddle.sety(y)


def leftplayerdown():
    y = leftPaddle.ycor()
    y = y - 40
    leftPaddle.sety(y)


def rightplayerup():
    y = rightPaddle.ycor()
    y = y + 40
    rightPaddle.sety(y)


def rightplayerdown():
    y = rightPaddle.ycor()
    y = y - 40
    rightPaddle.sety(y)

# Declarations
playerAScore = 0
playerBScore = 0
bounces = 0
ballSpeed = 1

# Make the screen
window = t.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=800)
window.tracer(1, 0)
t.delay(0)

# Left Paddle
leftPaddle = t.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("white")
leftPaddle.shapesize(stretch_wid=5, stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-350, 0)

# Right Paddle
rightPaddle = t.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color("white")
rightPaddle.shapesize(stretch_wid=5, stretch_len=1)
rightPaddle.penup()
rightPaddle.goto(350, 0)

# Ball
ball = t.Turtle()
ball.shape("circle")
ball.color("white")
ball.speed(3)
ball.pen(speed=1)
ball.penup()
ball.goto(0, 0)
ballXDirection = 0.2
ballYDirection = 0.2

board = t.Turtle()
board.speed(0)
board.color("white")
board.penup()
board.hideturtle()
board.goto(0, 260)
board.write(
    "                          Score \nPlayer A: {}      Bounces: {}      Player B: {} \n                          Speed = {} ".format(
        0, 0, 0, 0), align="center")
window.listen()
window.onkeypress(leftplayerup, 'w')
window.onkeypress(leftplayerdown, 's')
window.onkeypress(rightplayerup, 'Up')
window.onkeypress(rightplayerdown, 'Down')

while True:
    window.update()

    ball.setx(ball.xcor() + ballXDirection)
    ball.sety(ball.ycor() + ballYDirection)
    # Border set up
    # Vertical
    if ball.ycor() > 290:
        ball.sety(290)
        ballYDirection = ballYDirection * -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ballYDirection = ballYDirection * -1

    # Horizontal
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.pen(speed=1)
        ballXDirection = ballXDirection * -1
        playerAScore = playerAScore + 1
        bounces = 0
        # Score
        board.clear()
        board.write(
            "                          Score \nPlayer A: {}      Bounces: {}      Player B: {} \n                          Speed = {} ".format(
                playerAScore, bounces, playerBScore, bounces + 1), align="center")

    if (ball.xcor()) < -390:
        ball.goto(0, 0)
        ball.pen(speed=1)
        ballXDirection = ballXDirection * -1
        playerBScore = playerBScore + 1
        bounces = 0
        # Score
        board.clear()
        board.write(
            "                          Score \nPlayer A: {}      Bounces: {}      Player B: {} \n                          Speed = {} ".format(
                playerAScore, bounces, playerBScore, bounces + 1), align="center")

    # Collisions
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (
            rightPaddle.ycor() + 40 > ball.ycor() > rightPaddle.ycor() - 40):
        ball.setx(340)
        ballXDirection = ballXDirection * -1

        # High bounce difficulty
        if bounces % 1 == 0:
            ball.pen(speed=(ballSpeed + bounces + 1))
        bounces = bounces + 1

        board.clear()
        board.write(
            "                          Score \nPlayer A: {}      Bounces: {}      Player B: {} \n                          Speed = {} ".format(
                playerAScore, bounces, playerBScore, bounces + 1), align="center")

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (
            leftPaddle.ycor() + 40 > ball.ycor() > leftPaddle.ycor() - 40):
        ball.setx(-340)
        ballXDirection = ballXDirection * -1

        # High bounce difficulty
        if bounces % 1 == 0:
            ball.pen(speed=(ballSpeed + bounces + 1))
        bounces = bounces + 1

        board.clear()
        board.write(
            "                          Score \nPlayer A: {}      Bounces: {}      Player B: {} \n                          Speed = {} ".format(
                playerAScore, bounces, playerBScore, bounces + 1), align="center")