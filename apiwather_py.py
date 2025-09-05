import requests

API_KEY = '8794e6f224387c5adeb80fe37bdecd46'

cities = ['Mumbai', 'Delhi', 'Bengaluru', 'Pune', 'Kolkata', 'Pimpri', 'kolhapur', 'France', 'USA',]

def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temp = data['main']['temp']
        condition = data['weather'][0]['description'].title()
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        print(f"\n {city}")
        print(f" Temperature: {temp}°C")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind} m/s")

    except requests.exceptions.RequestException as e:
        print(f"\n  Could not fetch weather for {city}: {e}")

if __name__ == "__main__":
    print("Fetching live weather reports...\n")
    for city in cities:
        get_weather(city)