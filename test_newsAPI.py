import newsAPI

def test_newAPI():
    newsResponse = newsAPI.extract(0)
    assert newsResponse is not None 
    assert newsResponse['title'] is not None 
    assert newsResponse['content'] is not None