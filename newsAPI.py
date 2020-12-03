from apiHelper import get_news_URL
import requests
'''News API Extractions'''

def extract(article_index):
    '''Extracts'''
    url = (get_news_URL())
    response = requests.get(url)
    first_title = response.json()['articles'][article_index]['title']
    first_article = response.json()['articles'][article_index]['content']
    breaking_news =  {'title': first_title, 'content':first_article}
    return breaking_news

print(extract(0))
