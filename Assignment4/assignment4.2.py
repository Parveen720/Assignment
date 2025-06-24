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
        print(f"{temp}{chr(176)}")
        print(humidity)


    except requests.exceptions.RequestException as e:
        print(f" error fetch weather data:{e}")
city=input("enter the  city")
weather_details(city)