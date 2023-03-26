# from turtle import Turtle, Screen
import turtle
import random

sc_x = 500
sc_y = 400
sc = turtle.Screen()
sc.setup(width=sc_x, height=sc_y)
user_bet = sc.textinput(title="make user bet", prompt="choose bet")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# turtles = ["tim", "tima", "timi", "timu", "time", "timo"]
turtle_pos = ["-150", "-100", "-50", "0", "50", "100"]


all_turtles = []
for turtle_index in range(0, 6):
    _ = turtle.Turtle("turtle")
    _.color(colors[turtle_index])
    _.penup()
    _.goto(x=-230, y=int(turtle_pos[turtle_index]))
    all_turtles.append(_)


continue_flag = True
while continue_flag:
    for _ in all_turtles:
        _.forward(random.randint(0, 10))
        print(_.pos())
        if _.pos()[0] > 200:
            continue_flag = False
            print(_.color())

sc.exitonclick()
