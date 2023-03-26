import smtplib
import random
import datetime as dt

my_email = "yuukizinn@gmail.com"
password = "Gamester1"
app_password="nlmbrxqsntenezzm"

with open("/Users/yuuki/Documents/workspace/100_Days_of_Code/Day32_Birthday Wisher start/quotes.txt") as f:
	data= f.readlines()
msg = random.choice(data)

now = dt.datetime.now()
if now.weekday() == 4:
	with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
		connection.starttls()
		connection.login(user=my_email, password=app_password)
		connection.sendmail(
			from_addr=my_email,
			to_addrs="yuukizinn1@gmail.com",
			msg=f"Subject:test\n\n{msg}"
		)






