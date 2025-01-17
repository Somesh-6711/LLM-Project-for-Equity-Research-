from src.NewsGenius.utils.news_fetcher import fetch_top_headlines, fetch_articles_by_keyword

def get_news(category="general", country="us", keyword=None):
    """
    Combines fetching by category or keyword for unified interface.
    """
    if keyword:
        return fetch_articles_by_keyword(keyword)
    else:
        return fetch_top_headlines(category, country)
