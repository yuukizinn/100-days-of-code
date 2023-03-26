import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=800, height=600)
window.config(padx=200, pady=20)

def button_clicked():
	print("I got clicked")
	new_text = input.get()
	print(text.get("1.0", tkinter.END))
	my_label.config(text=new_text, padx=100)

def spinbox_used():
	print(spinbox.get())

def scale_used(value):
	print(value)

def checkbutton_used():
	print(checked_state.get())

def radio_used():
	print(radio_state.get())

def listbox_used(event):
	print(listbox.get(listbox.curselection()))

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=300, y=300)
my_label.grid(column=2, row=2)

my_label["text"] = "New Text"
my_label.config(text="New Text")

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=4)

input = tkinter.Entry(width=10)
input.insert(tkinter.END, string="Some text to bigin with.")
# input.pack()

text = tkinter.Text(height=5, width=30)
text.focus()
text.insert(tkinter.END, "Example of multi-line text entry.")
# text.pack()

spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

scale = tkinter.Scale(from_=0, to=100, command=scale_used)
# scale.pack()

checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
# checkbutton.pack()

radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()

listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
	listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()


window.mainloop()
