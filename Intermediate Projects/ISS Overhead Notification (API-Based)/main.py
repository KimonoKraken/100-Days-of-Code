import requests
from datetime import datetime
import smtplib
import time

# Seattle latitude and longitude
MY_LAT = 47.606209
MY_LONG = -122.332069

# Email credentials
MY_EMAIL = "dimitriyk25@gmail.com"
MY_PASSWORD = "CLEARED"

# International Space Station API longitude/latitude data
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Parameters based on sunrise-sunset API documentation
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# Formats sunrise and sunset of MY_LAT and MY_LONG to display only the hour value
sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

# Converts sunrise and sunset hour to seattle time
seattle_sunrise = sunrise_hour - 7
seattle_sunset = sunset_hour - 7
if seattle_sunset < 0:
    seattle_sunset = 24 + seattle_sunset

time_now = datetime.now()
current_hour = time_now.hour


# Function to see if ISS is +/- 5 latitude and longitude from my position, and if it is nighttime at my position
def iss_visible():
    if (MY_LAT - 5 < iss_latitude < MY_LAT + 5) \
            and (MY_LONG - 5 < iss_longitude < MY_LONG + 5) \
            and (seattle_sunset <= current_hour <= 24 or seattle_sunrise >= current_hour >= 0):
        return True


# Runs below code every 60 minutes
monitoring_ISS = True
while monitoring_ISS:
# If ISS is visible, sends me an email to let me know
    if iss_visible():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:LOOK UP for the ISS!!!!!\n\nThe ISS is above you!"
                                )

    time.sleep(60 * 60)




