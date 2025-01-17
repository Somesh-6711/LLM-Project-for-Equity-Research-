import streamlit as st

def display_articles(articles):
    """
    Displays a list of articles on the Streamlit interface.
    """
    for article in articles:
        st.subheader(article.get('title', 'No Title'))
        st.write(article.get('description', 'No Description'))
        st.markdown(f"[Read more]({article.get('url', '#')})")
