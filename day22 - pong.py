from turtle import Turtle, Screen
from day22.paddle import Paddle
from day22.ball import Ball
from day22.scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("slategrey")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

# draw center line
centerline = Turtle()
centerline.color("white")
centerline.penup()
centerline.hideturtle()
centerline.setpos(0,300)
centerline.width(5)
centerline.setheading(270)
for x in range(10):
    centerline.pendown()
    centerline.forward(30)
    centerline.penup()
    centerline.forward(30)

ball = Ball()
scoreboard = Scoreboard()
left_paddle = Paddle("left")
right_paddle = Paddle("right")
screen.update()
screen.listen()
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

game_on = True

while game_on:
    screen.update()
    ball.move()

    #top/bottom wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # paddle collision
    if ball.distance(left_paddle) < 50 and ball.xcor() > -350 or \
         ball.distance(right_paddle) < 50 and ball.xcor() < 350:
        ball.bounce_x()

    #goal collision
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

screen.exitonclick()