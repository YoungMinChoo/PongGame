import turtle as t
import winsound

# Declarations
ball_speed = 1
base_speed = 0.4
playerAScore, playerBScore = 0, 0
bounces = 0
menu = True
paused = False
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
leftPaddle.hideturtle()

# Right Paddle
rightPaddle = t.Turtle()
rightPaddle.penup()
rightPaddle.hideturtle()

# Ball
ball = t.Turtle()
ball.penup()
ball.hideturtle()

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
    pen.begin_fill()
    for i in range(2):
        pen.color("Red")
        pen.pensize(4)
        pen.pendown()
        pen.forward(length)
        pen.right(90)
        pen.forward(width)
        pen.right(90)
        pen.fillcolor("pink")

    pen.end_fill()
    pen.color("Black")
    pen.pensize(1)
    pen.penup()


def toggle_pause():
    global paused
    if menu:
        window.bye()
    elif not menu and not paused:
        paused = True
    else:
        paused = False
        action()



def clear_drawings():
    pen.clear()
    board.clear()
    leftPaddle.clear()
    rightPaddle.clear()
    ball.clear()


def btnclick(x,y):
    global menu
    if 37 < x < 157 and 47 > y > 12:
        print("Start Game")
        clear_drawings()
        in_game_env_setup()
        menu = False
    elif 37 < x < 157 and -33 > y > -68:
        print("Rules")
        # clear_drawings()
        # menu = False
    elif 37 < x < 157 and -113 > y > -148:
        print("Highscore")
        # clear_drawings()
        # menu = False
    elif 37 < x < 157 and -193 > y > -223:
        window.bye()
    print(x, y)


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
    if not paused:
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
    else:
        window.update()

# Draw main menu and buttons
pen.goto(37, 47)
pen.setheading(0)
button(120, 35)
pen.goto(45, 20)
pen.write("START GAME!", font=("Arial",12,"bold"))

pen.goto(37, -33)
pen.setheading(0)
button(120, 35)
pen.goto(45, -60)
pen.write("RULES", font=("Arial",12,"bold"))

pen.goto(37, -113)
pen.setheading(0)
button(120, 35)
pen.goto(45, -140)
pen.write("HIGH SCORE", font=("Arial",12,"bold"))

pen.goto(37, -193)
pen.setheading(0)
button(120, 35)
pen.goto(45, -220)
pen.write("QUIT", font=("Arial",12,"bold"))
#
window.onscreenclick(btnclick, 1)

# add function for different menus depending on if in game or main menu
window.onkeypress(toggle_pause, 'Escape')

window.listen()


t.mainloop()
