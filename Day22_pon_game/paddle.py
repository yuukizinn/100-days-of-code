from turtle import Turtle

class Paddle(Turtle):

	def __init__(self, pos):
		super().__init__()
		self.shape("square")
		self.penup()
		self.color("white")
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.goto(pos)

	def go_up(self):
		if self.ycor() < 260:
			new_y = self.ycor() + 20
			self.goto(self.xcor(), new_y)

	def go_down(self):
		if self.ycor() > -250:
			new_y = self.ycor() - 20
			self.goto(self.xcor(), new_y)
