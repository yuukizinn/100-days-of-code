from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):


	def __init__(self):
		super().__init__()
		self.score = 0
		self.high_score = 0
		with open("data.txt", mode="r") as data:
			self.high_score = int(data.read())
		self.penup()
		self.hideturtle()
		self.goto(x = 0, y = 260)
		self.color("white")
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear()
		self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score
			with open("data.txt", mode="w") as data:
				data.write(str(self.high_score))
		self.score = 0
		self.update_scoreboard()

	# def game_over(self):
	# 	self.goto(x = 0, y = 0)
	# 	self.write(f"GameOver", align=ALIGNMENT, font=FONT)

	def add_point(self):
		self.score += 1
		self.update_scoreboard()
