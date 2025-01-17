import requests
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv('NEWS_API_KEY')

def fetch_top_headlines(category="general", country="us", page_size=10):
    """
    Fetches top headlines based on category and country.
    """
    url = f"https://newsapi.org/v2/top-headlines?category={category}&country={country}&pageSize={page_size}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('articles', [])
    else:
        response.raise_for_status()

def fetch_articles_by_keyword(keyword, page_size=10):
    """
    Fetches articles based on the provided keyword.
    """
    url = f"https://newsapi.org/v2/everything?q={keyword}&pageSize={page_size}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('articles', [])
    else:
        response.raise_for_status()
