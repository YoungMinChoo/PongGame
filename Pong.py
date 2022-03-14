import turtle as t
import winsound

# Declarations
ball_speed = 1
base_speed = 0.4
playerAScore, playerBScore = 0, 0
bounces = 0
menu = True
ballXDirection, ballYDirection = base_speed, base_speed

# Initializations

# Make the screen
window = t.Screen()
window.title("Pong Game")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)

# Pen for writing
pen = t.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

# Left Paddle
leftPaddle = t.Turtle()
leftPaddle.penup()
# leftPaddle.hideturtle()

# Right Paddle
rightPaddle = t.Turtle()
rightPaddle.penup()
# rightPaddle.hideturtle()

# Ball
ball = t.Turtle()
ball.penup()
# ball.hideturtle()

# Scoreboard
board = t.Turtle()
board.speed(0)
board.color("white")
board.penup()
board.hideturtle()


# Functions

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


# Menu Buttons
def button(length, width):
    for i in range(2):
        pen.forward(length)
        pen.left(90)
        pen.forward(width)
        pen.left(90)


def clear_drawings():
    pen.clear()
    board.clear()
    leftPaddle.clear()
    rightPaddle.clear()
    ball.clear()
    # window.clear()


def btnclick(x,y):
    global menu
    if 0 < x < 101 and 0 > y > -101:
        print("Start Game")
        print(x, y)
        clear_drawings()
        in_game_env_setup()
    elif 0 < x < 101 and -101 > y > -201:
        print("Rules")
        print(x, y)
        clear_drawings()
    elif 0 < x < 101 and -201 > y > -301:
        print("Highscore")
        print(x, y)
        clear_drawings()
    elif 0 < x < 101 and -301 > y > -401:
        print("Hi")
        print(x, y)
        clear_drawings()
    elif 0 < x < 101 and -401 > y > -501:
        print("Hi")
        print(x, y)
        clear_drawings()
    elif 0 < x < 101 and -501 > y > -601:
        print("Hi")
        print(x, y)
        clear_drawings()
    menu = False
    return menu


def in_game_env_setup():
    window.bgcolor("black")

    ball.shape("circle")
    ball.color("white")
    ball.speed(0)
    ball.goto(0, 0)

    leftPaddle.speed(0)
    leftPaddle.shape("square")
    leftPaddle.color("white")
    leftPaddle.shapesize(stretch_wid=5, stretch_len=1)
    leftPaddle.goto(-350, 0)

    rightPaddle.speed(0)
    rightPaddle.shape("square")
    rightPaddle.color("white")
    rightPaddle.shapesize(stretch_wid=5, stretch_len=1)
    rightPaddle.goto(350, 0)

    board.goto(0, 260)
    board.write(
    "                          Score \nPlayer A: {}      Bounces: {}      Player B: {} \n                          Speed = {} ".format(
        0, 0, 0, 1), align="center")

    # Controls
    window.listen()
    window.onkeypress(leftplayerup, 'w')
    window.onkeypress(leftplayerdown, 's')
    window.onkeypress(rightplayerup, 'Up')
    window.onkeypress(rightplayerdown, 'Down')

    action()


def action():
    global playerAScore, playerBScore, bounces, ballXDirection, ballYDirection, ball_speed
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
        ballXDirection, ballYDirection = base_speed, base_speed
        ballXDirection = ballXDirection * -1
        playerAScore = playerAScore + 1
        bounces = 0
        ball_speed = 1

        # Score
        board.clear()
        board.write(
            "                          Score \nPlayer A: {}      Bounces: {}      Player B: {} \n                          Speed = {} ".format(
                playerAScore, bounces, playerBScore, bounces + 1), align="center")

    if (ball.xcor()) < -390:
        ball.goto(0, 0)
        ballXDirection, ballYDirection = base_speed, base_speed
        ballXDirection = ballXDirection * -1
        playerBScore = playerBScore + 1
        bounces = 0
        ball_speed = 1

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
        bounces = bounces + 1

        # High bounce difficulty
        if bounces % 2 == 0:
            ballXDirection *= 1.2
            ballYDirection *= 1.2
            ball_speed += 1

        # Score
        board.clear()
        board.write(
            "                          Score \nPlayer A: {}      Bounces: {}      Player B: {} \n                          Speed = {} ".format(
                playerAScore, bounces, playerBScore, ball_speed), align="center")

    elif (ball.xcor() < -340) and (ball.xcor() > -350) and (
            leftPaddle.ycor() + 40 > ball.ycor() > leftPaddle.ycor() - 40):
        ball.setx(-340)
        ballXDirection = ballXDirection * -1
        bounces = bounces + 1

        # High bounce difficulty
        if bounces % 2 == 0:
            ballXDirection *= 1.2
            ballYDirection *= 1.2
            ball_speed += 1

        board.clear()
        board.write(
            "                          Score \nPlayer A: {}      Bounces: {}      Player B: {} \n                          Speed = {} ".format(
                playerAScore, bounces, playerBScore, ball_speed), align="center")

    window.ontimer(action, 1)

# Draw menu
pen.goto(8, -46)
pen.write("START GAME!", font=("Arial",12,"normal"))

pen.goto(6, -145)
pen.write("RULES", font=("Arial",12,"normal"))

pen.goto(3, -248)
pen.write("HIGH SCORE", font=("Arial",12,"normal"))

pen.goto(4, -343)
pen.write("QUIT", font=("Arial",12,"normal"))

#
window.onscreenclick(btnclick, 1)
window.listen()


t.mainloop()
