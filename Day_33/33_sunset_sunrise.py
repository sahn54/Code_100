import requests
from datetime import datetime
NY_LATITUDE = 40.736881
NY_LONGITUDE = -73.816681

MY_LAT = 51.507351
MY_LNG = -0.127758

parameters = {
    "lat": NY_LATITUDE,
    "lng": NY_LONGITUDE,
    "formatted": 0  # AM/PM formatted(1), 24hr formatted(0)
}

# for this API we need parameters - we add params
response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split('T')[1].split(':')[0]
sunset = data["results"]["sunset"].split('T')[1].split(':')[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
