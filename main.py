import requests, json

api_key = "2bfb4fa790e4d50048c8dc8650a4fe68"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter City Name : ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":
    y = x["main"]

    current_temp = y["temp"]
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]

    z = x["weather"]
    weather_description = z[0]["description"]

    output = ("Temperature (in kelvin) = " +
                    str(current_temp) +
              "\n Atmospheric Pressure (in hPa) = " +
                    str(current_pressure) +
              "\n Humidity (in percentage) = " +
                    str(current_humidity) +
              "\n Description = " +
                    str(weather_description) +
              "\n -------------------------- \n")

    with open("out.txt", "a") as f:
        f.write(output)

else:
    print("City Not Found")