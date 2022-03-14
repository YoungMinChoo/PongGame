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

# Menu pen
menu_pen = t.Turtle()
menu_pen.speed(0)
menu_pen.penup()
menu_pen.hideturtle()

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
def button(length, width, a_pen):
    a_pen.begin_fill()
    for i in range(2):
        a_pen.color("Red")
        a_pen.pensize(4)
        a_pen.pendown()
        a_pen.forward(length)
        a_pen.right(90)
        a_pen.forward(width)
        a_pen.right(90)
        a_pen.fillcolor("pink")

    a_pen.end_fill()
    a_pen.color("Black")
    a_pen.pensize(1)
    a_pen.penup()


def toggle_pause():
    global paused
    if menu:
        window.bye()
    elif not menu and not paused:
        paused = True
        pause_menu()
    else:
        paused = False
        pause_menu()


def main_menu():
    window.bgcolor("White")
    # Draw main menu and buttons
    pen.goto(37, 47)
    pen.setheading(0)
    button(120, 35, pen)
    pen.goto(45, 20)
    pen.write("START GAME!", font=("Arial",12,"bold"))

    pen.goto(37, -33)
    pen.setheading(0)
    button(120, 35, pen)
    pen.goto(45, -60)
    pen.write("RULES", font=("Arial",12,"bold"))

    pen.goto(37, -113)
    pen.setheading(0)
    button(120, 35, pen)
    pen.goto(45, -140)
    pen.write("HIGH SCORE", font=("Arial",12,"bold"))

    pen.goto(37, -193)
    pen.setheading(0)
    button(120, 35, pen)
    pen.goto(45, -220)
    pen.write("QUIT", font=("Arial",12,"bold"))


def pause_menu():
    if paused:
        # Hide the elements in game
        ball.hideturtle()
        leftPaddle.hideturtle()
        rightPaddle.hideturtle()

        # Draw the menu box
        menu_pen.goto(-380, 290)
        button(750, 550, menu_pen)

        # Draw buttons
        menu_pen.goto(37, 47)
        menu_pen.setheading(0)
        button(200, 35, menu_pen)
        menu_pen.goto(45, 20)
        menu_pen.write("Back to Main Menu", font=("Arial",12,"bold"))

        menu_pen.goto(37, -33)
        menu_pen.setheading(0)
        button(120, 35, menu_pen)
        menu_pen.goto(45, -60)
        menu_pen.write("Unpause", font=("Arial",12,"bold"))


    else:
        menu_pen.clear()
        ball.showturtle()
        leftPaddle.showturtle()
        rightPaddle.showturtle()
        action()


def clear_drawings():
    menu_pen.clear()
    pen.clear()
    board.clear()
    leftPaddle.clear()
    rightPaddle.clear()
    ball.clear()


def btnclick(x,y):
    global menu
    # if in main menu
    if menu:
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

    # if in pause menu
    else:
        if 37 < x < 157 and 47 > y > 12:
            print("Back to Main Menu")
            clear_drawings()
            menu = True
            main_menu()
        elif 37 < x < 157 and -33 > y > -68:
            print("Unpause")
            # clear_drawings()
            # menu = False


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


main_menu()
window.onscreenclick(btnclick, 1)

# add function for different menus depending on if in game or main menu
window.onkeypress(toggle_pause, 'Escape')

window.listen()


t.mainloop()
