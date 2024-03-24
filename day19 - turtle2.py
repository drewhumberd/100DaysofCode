from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)

# Turtle Racing
is_race_on = False

user_bet = screen.textinput(title="Make your bets!",
                            prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []

def make_turtle(name, color, ypos):
    name = Turtle(shape="turtle")
    name.color(color)
    name.penup()
    name.goto(-230, ypos)
    all_turtles.append(name)

topline = 166
for x in colors:
    make_turtle(x, x, topline)
    topline -= 66

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winning turtle is the {winning_color} turtle!")
            else:
                print(f"You've lost! The {winning_color} turtle won the race.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Etch-a-Sketch
# def move_forward():
#     tim.forward(10)

# def move_backward():
#     tim.backward(10)

# def turn_left():
#     tim.left(10)

# def turn_right():
#     tim.right(10)

# def clear():
#     tim.reset()

# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear)

screen.exitonclick()