import requests
import time
from datetime import datetime
import smtplib

MY_LAT = 28.704060  # Your latitude
MY_LONG = 77.102493  # Your longitude
my_email = 'abcd@gmail.com'
my_pass = 'abcd123'


def check_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (MY_LAT - 5) <= iss_latitude and iss_latitude <= (MY_LAT + 5) and (
            MY_LONG - 5) <= iss_longitude and iss_longitude <= (MY_LONG + 5):
        return True


def check_night():
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
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if check_iss() and check_night():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(my_email, my_pass)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:Look up\n The ISS Satellite above you")
