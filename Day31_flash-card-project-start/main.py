from tkinter import *
import pandas
import random
import os

os.chdir("/Users/yuuki/Documents/workspace/100_Days_of_Code/Day31_flash-card-project-start")

BACKGROUND_COLOR = "#B1DDC6"

choice = {}
word_dict = {}

try:
	data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
	original_data = pandas.read_csv("data/french_words.csv")
	word_dict = original_data.to_dict(orient="records")
else:
	word_dict = data.to_dict(orient="records")

def next_card():
	global choice, flip_timer
	window.after_cancel(flip_timer)
	choice = random.choice(word_dict)
	canvas.itemconfig(card_title, text="French", fill="black")
	canvas.itemconfig(card_word, text=choice["French"], fill="black")
	canvas.itemconfig(canvas_image, image=front_image)
	flip_timer = window.after(3000, func=flip_card)

def flip_card():
	canvas.itemconfig(card_title, text="English", fill="white")
	canvas.itemconfig(card_word, text=choice["English"], fill="white")
	canvas.itemconfig(canvas_image, image=back_image)

def is_known():
	word_dict.remove(choice)
	print(len(word_dict))
	data = pandas.DataFrame(word_dict)
	data.to_csv("data/words_to_learn.csv", index=False)
	next_card()

#----- UI SETTING -----#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
card_title = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

flip_timer = window.after(3000, func=flip_card)
next_card()

window.mainloop()
