import json

config = {
    'weather_api': {
        'baseURL': 'http://api.openweathermap.org/data/2.5/weather',
        'appid': 'f9f7a6256b5b4b32c161b9477539edef'
        },
    'news_api': {
        'baseURL': 'http://newsapi.org/v2/top-headlines',
        'apiKey': '1fa75a8b1d3b4f519edbd51156853cf8'
    }
}

with open('config.json', 'w') as f:
    json.dump(config, f)