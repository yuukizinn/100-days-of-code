from tkinter import *

FONT = ("Arial", 24, "bold")

window = Tk()
window.title("")
window.minsize(width=400, height=300)
window.config(padx=20, pady=20)

entry_miles = Entry(width=7)
entry_miles.grid(row=0, column=1)

label_miles = Label(text="Miles", font=FONT)
label_miles.grid(row=0, column=2)

label_is_equal_to = Label(text="is equal to", font=FONT)
label_is_equal_to.grid(row=1, column=0)

label_answer = Label(text = 0, font = FONT)
label_answer.grid(row=1, column=1)

label_km = Label(text="Km", font=FONT)
label_km.grid(row=1, column=2)

def click_button():
	value = float(entry_miles.get())
	culc = round(value * 1.6, 2)
	label_answer.config(text=culc)
	print(culc)


button_calculate = Button(text="Culculate", font=FONT, command=click_button)
button_calculate.grid(row=2, column=1)

window.mainloop()

