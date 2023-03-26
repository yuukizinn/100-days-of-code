import os
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

os.chdir("/Users/yuuki/Documents/workspace/100_Days_of_Code/Day29_password-manager-start")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
	password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
	password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
	password_list = password_letters + password_symbols + password_numbers
	random.shuffle(password_list)
	password = "".join(password_list)
	password_entry.insert(0, password)
	pyperclip.copy(password)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
	website = website_entry.get()
	try:
		with open("data.json", mode="r") as f:
			data = json.load(f)
	except FileNotFoundError:
		messagebox.showinfo(message="No Data File Found.")
	else:
		if website in data:
			email = data[website]["email"]
			password = data[website]["password"]
			messagebox.showinfo(title=website, message=f"email: {email} \npassword: {password}")
		else:
			messagebox.showinfo(message="No Details for the website exists.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
	website = website_entry.get()
	email = email_entry.get()
	password = password_entry.get()
	new_data = {
		website: {
			"email": email,
			"password": password
		}
	}

	if len(website) == 0 or len(password) == 0:
		messagebox.showinfo(title="aaa", message="Please don't leave any fields empty!")
	else:
		try:
			with open("data.json", mode="r") as f:
				data = json.load(f)
		except FileNotFoundError:
			with open("data.json", mode="w") as f:
				json.dump(new_data, f, indent=4)
				# data = json.load(f)
		else:
			data.update(new_data)
			with open("data.json", mode="w") as f:
				json.dump(data, f, indent=4)
		finally:
			website_entry.delete(0, END)
			password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="/Users/yuuki/Documents/workspace/100_Days_of_Code/Day29_password-manager-start/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "yuukizinn@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
