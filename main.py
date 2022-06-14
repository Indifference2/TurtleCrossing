import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    if player.check_turtle_cross_the_road():
        player.reset_position()
        scoreboard.increase_level()
        car_manager.increase_speed()
    if car_manager.check_car_collision_with_turtle(player):
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
