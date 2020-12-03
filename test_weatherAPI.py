import weatherAPI

def test_weatherAPI():
    newsResponse = weatherAPI.weather_today()
    assert newsResponse is not None 
    assert newsResponse['title'] is not None 
    assert newsResponse['content'] is not None