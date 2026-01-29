import requests

def get_weather(city):

    API_KEY="MY_API KEY"
    URL=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(URL) 
        data = response.json()
        if response.status_code == 200:
            print(f" weather in {data['name']},{data['sys']['country']}:")
            print(f" temperature: {data['main']['temp']}ºC")
            print(f" Humidity:{data['main']['humidity']}% ")
            print(f" weather: {data['weather'][0]['description']}")
            print(f" wind speed: {data['wind']['speed']}m/s ")
        else:
            print(f"city{city} not found, please check the name and try again..")
    except Exception as e:
        print(f"something went wrong: {e}")
    
if __name__ =="__main__":
    city = input("enter the city name :")
    get_weather(city)
