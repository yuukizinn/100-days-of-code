from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_forward, "Up")

game_is_on = True
while game_is_on:
	time.sleep(0.1)
	screen.update()

	if 0.9 < random.random():
		CarManager()

	for car in cars.car_lists:
		car.go_forward()
		if car.distance(player) < 20:
			game_is_on = False
			scoreboard.game_over()

	if player.goal():
		scoreboard.level_up()
		for car in cars.car_lists:
			car.level_up()
