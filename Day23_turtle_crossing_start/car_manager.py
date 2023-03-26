from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITION = [(300, 100), (300, 150), (), ]

class CarManager(Turtle):

	movespeed = STARTING_MOVE_DISTANCE
	car_lists = []

	def __init__(self):
		super().__init__()
		self.shape("square")
		self.penup()
		self.shapesize(stretch_wid=1, stretch_len=2)
		# self.color(COLORS[random.randint(0, 5)])
		self.color(random.choice(COLORS))
		self.goto(280, random.randint(-200, 280))
		CarManager.car_lists.append(self)

	def go_forward(self):
		new_x = self.xcor() - CarManager.movespeed
		self.goto(new_x, self.ycor())

	def level_up(self):
		CarManager.movespeed += MOVE_INCREMENT

