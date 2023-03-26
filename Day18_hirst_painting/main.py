import colorgram
import random
from turtle import Turtle, Screen


def pick_color(image):
    colors = colorgram.extract(image, 100)
    c_list = []
    for color in colors:
        rgb = color.rgb # e.g. (255, 151, 210)
        c_list.append((rgb.r, rgb.g, rgb.b))
    return c_list


color_list = pick_color('/Users/yuuki/Documents/workspace/100_Days_of_Code/Day18_hirst_painting/image.jpg')

tim = Turtle()
tim.shape("turtle")
tim.speed(0)
tim.penup()
sc = Screen()
sc.colormode(255)

x = -300
y = -300
for _ in range(7):
    x = -300
    for _ in range(7):
        tim.color(random.choice(color_list))
        tim.setposition(x, y)
        tim.dot(50)
        x = x + 100
    y = y + 100


sc.exitonclick()


# red = rgb[0]
# red = rgb.r
