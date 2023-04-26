import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)


# if response.status_code != 200:
#     raise Exception("Bad response from ISS API")

# if response.status_code == 404:
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to access this data.")
# instead above, use this method instead:

response.raise_for_status()

data = response.json()
print(data)
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)

# reference: httpstatuses.com ,latlong.net

# status_code:
# 1XX: Hold On
# 2XX: Here You Go
# 3XX: Go Away
# 4XX: You Screwed up
# 5XX: I Screwed up
