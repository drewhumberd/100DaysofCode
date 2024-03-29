import time
from turtle import Screen
from day23.player import Player
from day23.car_manager import CarManager
from day23.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()
carmanager = CarManager()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    carmanager.create_car()
    carmanager.move()
    for car in carmanager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
    if player.check_at_end():
        scoreboard.score_up()
        carmanager.level_up()
        player.return_to_start()
    screen.update()

screen.exitonclick()