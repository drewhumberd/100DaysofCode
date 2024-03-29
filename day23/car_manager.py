from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = randint(1, 6)
        if chance == 1:
            car = Turtle()
            car.color(choice(COLORS))
            car.setheading(180)
            car.shape("square")
            car.resizemode("user")
            car.shapesize(1,2,0)
            car.penup()
            random_y = randint(-250, 250)
            car.goto(300, random_y)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.carspeed)

    def level_up(self):
        self.carspeed += MOVE_INCREMENT
