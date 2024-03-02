from turtle import Screen, Turtle
import time
from Score import ScoreB
from Paddle import PaddleB
from ball import Ball
from background import Background
LEFT_PADDLE = [(-280, 0)]
RIGHT_PADDLE = [(280, 0)]

# Variables

screen = Screen()
tim1 = Turtle()
right_score = ScoreB()
left_score = ScoreB()
paddle1 = PaddleB(280, 0)
paddle2 = PaddleB(-280, 0)
baller = Ball()
backG = Background()

# Score Set_up

right_score.goto(60, 280)
left_score.goto(-60, 280)
right_score.set_score()
left_score.set_score()

# Setting up Screen

should_continue = True

screen.setup(width=600, height =600)
screen.bgcolor("black")
screen.tracer(0)


# Setting up controls
screen.listen()
screen.onkeypress(paddle1.up, "Up")
screen.onkeypress(paddle1.down, "Down")
screen.onkeypress(paddle2.up, "w")
screen.onkeypress(paddle2.down, "s")


while should_continue:
    screen.update()
    baller.move()
    time.sleep(baller.move_speed)
    # Collisions on the wall
    if baller.ycor() > 280 or baller.ycor() < -280:
        baller.bounce_y()

    paddle1.move()
    paddle2.move()
#      collisions with  right paddle
    if baller.distance(paddle1) < 50 and baller.xcor() > 240 or baller.distance(paddle2) < 50 and baller.xcor() < -240:
        baller.bounce_x()

#    detect paddle miss
    if baller.xcor() > 320:
        baller.reset_position()
        left_score.set_score()

    if baller.xcor() < -320:
        baller.reset_position()
        right_score.set_score()

    if right_score.score == 3 or left_score.score == 3:
        should_continue = False



screen.exitonclick()
