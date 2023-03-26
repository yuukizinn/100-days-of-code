import requests
from datetime import datetime

MY_LAT = -219.874191
MY_LONG = 35.651159

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour


if (((MY_LAT + 5) > iss_latitude or iss_longitude < (MY_LAT - 5)) and
    ((MY_LONG + 5) > iss_longitude or iss_longitude < (MY_LONG - 5))):
    if sunrise < time_now and time_now > sunset:
        #sendemail
        pass

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

