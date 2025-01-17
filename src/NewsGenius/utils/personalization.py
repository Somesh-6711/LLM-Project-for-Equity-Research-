import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

PREFERENCES_FILE = "config/user_preferences.json"

def save_user_preferences(preferences):
    """
    Saves user preferences to a JSON file.
    """
    os.makedirs(os.path.dirname(PREFERENCES_FILE), exist_ok=True)
    with open(PREFERENCES_FILE, "w") as f:
        json.dump(preferences, f)

def load_user_preferences():
    """
    Loads user preferences from a JSON file.
    """
    if os.path.exists(PREFERENCES_FILE):
        with open(PREFERENCES_FILE, "r") as f:
            return json.load(f)
    return {}

def recommend_articles(user_keywords, articles):
    """
    Recommends articles based on user preferences.
    """
    article_texts = [article['title'] + " " + article['description'] for article in articles]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(user_keywords + article_texts)
    similarities = cosine_similarity(tfidf_matrix[0:len(user_keywords)], tfidf_matrix[len(user_keywords):])
    recommendations = sorted(list(enumerate(similarities.sum(axis=0))), key=lambda x: x[1], reverse=True)
    return [articles[i[0]] for i in recommendations[:5]]
