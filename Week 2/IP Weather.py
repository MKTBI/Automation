import requests


ip_address = input("Enter an IP address: ")
geo_url = f"https://get.geojs.io/v1/ip/geo/{ip_address}.json"
response = requests.get(geo_url)
data = response.json()

lat = data["latitude"]
lon = data["longitude"]
weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
response = requests.get(weather_url)
data = response.json()
print(data)

# print weather information
#for hour in data['hours']:
 #   print(f"Time: {hour['time']} Temperature: {hour['temperature']} Weather: {hour['weather']['description']}")
