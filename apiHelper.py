import json

config = {}
with open('config.json', 'r') as f:
    config = json.load(f)

def get_weather_URL(location = 'exeter', units = 'metric'):
    return config['weather_api']['baseURL'] + '?' + f'appid={config["weather_api"]["appid"]}'+ f'&q={location}'+ f'&units={units}'

def get_news_URL(country = 'us'):
    return config['news_api']['baseURL'] + '?' + f'apiKey={config["news_api"]["apiKey"]}'+ f'&country={country}' 