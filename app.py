import streamlit as st
from utils.news_fetcher import fetch_top_headlines, fetch_articles_by_keyword
from utils.personalization import save_user_preferences, load_user_preferences, recommend_articles
from utils.interface import display_articles

st.title("Personalized News Research Tool")

st.sidebar.title("User Preferences")
keywords = st.sidebar.text_input("Enter keywords (comma-separated):").split(',')

category = st.sidebar.selectbox("Select news category", ["general", "business", "technology", "sports", "health", "entertainment", "science"])
country = st.sidebar.text_input("Country code (default: us)", "us")

if st.sidebar.button("Save Preferences"):
    save_user_preferences({"keywords": keywords, "category": category, "country": country})
    st.sidebar.success("Preferences saved!")

user_preferences = load_user_preferences()

if st.sidebar.button("Fetch News"):
    articles = fetch_top_headlines(category=user_preferences.get("category", "general"), country=user_preferences.get("country", "us"))
    st.header("Top Headlines")
    display_articles(articles)

if keywords:
    articles = fetch_articles_by_keyword(keywords[0])
    recommendations = recommend_articles(keywords, articles)
    st.header("Recommended Articles")
    display_articles(recommendations)
