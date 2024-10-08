import requests

def get_weather(city):
    api_key = "8d6454a89dff871786a0307b0dbebbee" #You_API_key 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        print(f"Temperature: {temp}°C")
        print(f"Weather: {weather_desc}")
    else:
        print("City not found.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
