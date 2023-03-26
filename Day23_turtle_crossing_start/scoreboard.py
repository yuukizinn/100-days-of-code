from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-220, 260)

class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.level = 1
		self.penup()
		self.hideturtle()
		self.goto(POSITION)
		self.write(f"Level: {self.level}", False, align="center", font=FONT)

	def level_up(self):
		self.clear()
		self.level += 1
		self.write(f"Level: {self.level}", False, align="center", font=FONT)

	def game_over(self):
		self.goto(0, 0)
		self.write(f"Game Over", False, align="center", font=FONT)


