import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 37.5665,
    "longitude": 126.9780,
    "current_weather": True
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    temp = data['current_weather']['temperature']
    windspeed = data['current_weather']['windspeed']
    
    print(f"Current Temperature: {temp}°C")
    print(f"Wind Speed: {windspeed} km/h")

else:
    print(f"Error: {response.status_code}")