import os
import pandas
import random
import datetime as dt
import smtplib

os.chdir("/Users/yuuki/Documents/workspace/100_Days_of_Code/Day32_birthday-wisher-extrahard-start")
letter_templates = os.listdir("./letter_templates")

my_email = "yuukizinn@gmail.com"
app_password="nlmbrxqsntenezzm"

birthdays_data = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()

for (index, item) in birthdays_data.iterrows():
	if item["month"] == now.month and item["day"] == now.day:
		to_name = item["name"]
		to_email = item["email"]
		text_file = random.choice(letter_templates)
		with open(f"./letter_templates/{text_file}") as f:
			to_msg = f.read()
			to_msg = to_msg.replace("[NAME]", to_name)
		with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
			connection.starttls()
			connection.login(my_email, app_password)
			connection.sendmail(
				from_addr = my_email,
				to_addrs = to_email,
				msg=f"Subject:aaa\n\n{to_msg}"
			)
