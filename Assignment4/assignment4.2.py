import requests

def weather_details(city):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2e2cac1a891061ca51e204da2f9fc18b"
    final_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2e2cac1a891061ca51e204da2f9fc18b&units=metric"
    try:
        response=requests.get(final_url)
        response.raise_for_status() #if we not use ot  than it give error as other otherwise give url error
        data1=response.json()
#format of data json
        temp=data1["main"]["temp"]
        humidity=data1["main"]["humidity"]
        country=data1["sys"]["country"]
        print(f"{temp}{chr(176)}")
        print(humidity)
        print(country)


    except requests.exceptions.RequestException as e:
        print(f" error fetch weather data:{e}")
city=input("enter the  city")
weather_details(city)


# {"coord":{"lon":75.8167,"lat":26.9167},
#  "weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],
#  "base":"stations",
#  "main":{"temp":302.35,"feels_like":306.52,"temp_min":302.35,"temp_max":302.35,"pressure":1000,"humidity":71,"sea_level":1000,"grnd_level":954},
#  "visibility":10000,
#  "wind":{"speed":7.96,"deg":260,"gust":8.37},
#  "clouds":{"all":100},"dt":1750652531,
#  "sys":{"country":"IN","sunrise":1750637032,"sunset":1750686832},
#  "timezone":19800,
#  "id":1269515,
#  "name":"Jaipur",
#  "cod":200}
# temprature=data["coord"]["lon"]
# print(temprature)

#{"coord":{"lon":75.8167,"lat":26.9167},
# "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
# "base":"stations",
# "main":{"temp":29.18,"feels_like":36.18,"temp_min":29.18,"temp_max":29.18,"pressure":998,"humidity":89,"sea_level":998,"grnd_level":950},
# "visibility":10000,
# "wind":{"speed":1.13,"deg":213,"gust":1.53},
# "clouds":{"all":61},"dt":1750800216,"sys":{"country":"IN","sunrise":1750809861,"sunset":1750859651},"timezone":19800,"id":1269515,"name":"Jaipur","cod":200}