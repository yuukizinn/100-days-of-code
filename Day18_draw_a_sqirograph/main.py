import random
import turtle
from turtle import Turtle, Screen

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim = turtle.Turtle()
tim.shape("turtle")
tim.speed(0)


def num_of_edge(n_edge):
    angle = 360 / n_edge
    for _ in range(n_edge):
        tim.circle(100)
        tim.right(angle)


def random_walk(step_count):
    for _ in range(step_count):
        tim.color(random.choice(colours))
        n_edge = random.randint(1, 4)
        angle = 90 * n_edge
        tim.right(angle)
        tim.forward(25)


num_of_edge(30)

x = 0
for _ in range(85):
    tim.color(random.choice(colours))
    x = 10
    tim.circle(100)
    tim.penup()
    tim.right(x)
    tim.pendown()

for i in range(3, 10):
    tim.color(random.choice(colours))
    num_of_edge(i)

sc = Screen()
sc.exitonclick()
