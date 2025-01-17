from src.NewsGenius.utils.personalization import recommend_articles

def get_recommended_news(user_keywords, articles):
    """
    Fetch personalized recommendations.
    """
    return recommend_articles(user_keywords, articles)
