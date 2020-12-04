from apiHelper import get_weather_URL
import requests
'''Main Weather API'''

data = requests.get(get_weather_URL())
weather = data.json()

def weather_today():
    '''This function extracts relevent info from the API'''

    description = weather["weather"][0]["description"]
    temp = str(round(weather["main"]["temp"]))
    wind_dir = weather["wind"]["deg"]

    wind_compass_sector = (wind_dir+22.5) //45
    wind_compass_maping ={0:"north",1:"north-east", 2:"east", 3:"south-east", 4:"south", 5:"south-west", 6:"west", 7:"north-west"}
    wind_compass_dir = wind_compass_maping[wind_compass_sector]

    description_final = "The weather is " + description + " with a temperature of " + temp + " in degrees Celsius and wind blowing to the " + wind_compass_dir + "."

    notifications_dict =  {"title" :"Weather", "content": description_final}
    return notifications_dict

print(weather_today())
