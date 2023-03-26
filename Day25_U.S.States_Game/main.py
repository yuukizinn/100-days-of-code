from ast import NotIn
import os
import turtle
import pandas

os.chdir("/Users/yuuki/Documents/workspace/100_Days_of_Code/Day25_U.S.States_Game")

screen = turtle.Screen()
answer = 0
screen.title(f"{answer}/50 U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)


game_is_on = True
answer_list = []
df = pandas.read_csv("50_states.csv")

while len(answer_list) < 50:

	answer_state = screen.textinput(title="Guess the State", prompt="What's a another state's name?").capitalize()

	if answer_state == "Exit":
		break

	if answer_state in df["state"].values and answer_state not in answer_list:
		answer_list.append(answer_state)
		print(answer_list)
		x = int(df[df["state"] == answer_state].x.values)
		y = int(df[df["state"] == answer_state].y.values)
		new_answer = turtle.Turtle()
		new_answer.hideturtle()
		new_answer.penup()
		new_answer.goto(x, y)
		new_answer.write(answer_state, font=('Arial', 14, 'normal'))
		screen.update()
		answer += 1
		screen.title(f"{answer}/50 U.S. States Game")

states_to_learn = df["state"].to_list()
for state in answer_list:
	states_to_learn.remove(state)

df = pandas.DataFrame(states_to_learn, columns=["state"])
df.to_csv("states_to_learn.csv")
