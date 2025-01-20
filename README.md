# NewsGenius-LLM-Project-for-Equity-Research-
End to End Gen AI Project Using Langchain, OpenAI in Finance Domain;  a news research tool that can be used by equity research analysts to conduct their research.



## Overview
**NewsGenius** is a personalized news research tool designed to provide users with a seamless experience for exploring, analyzing, and interacting with news articles. It leverages APIs and cutting-edge technologies to fetch real-time news, recommend articles based on user preferences, and present them in a user-friendly interface. Whether you're a casual reader or a researcher, NewsGenius empowers you to stay informed and engaged.

---

## Features

1. **Real-Time News Fetching**
   - Fetch top headlines from various categories (e.g., general, business, technology, sports).
   - Search for articles using specific keywords.

2. **Personalized Recommendations**
   - Get tailored article suggestions based on your interests and reading history.

3. **User-Friendly Interface**
   - Intuitive design with Streamlit for seamless navigation.
   - Options to save and share news articles.

4. **Advanced Technologies**
   - **API Integration**: Uses OpenAI and NewsAPI for real-time data and natural language processing.
   - **Machine Learning**: Employs TF-IDF and cosine similarity for personalized recommendations.
   - **Configurable Settings**: Easily modify preferences such as country, categories, and keywords.

---

## How It Works

1. **Set Preferences**:
   - Choose your preferred news category (e.g., sports, technology).
   - Specify a country for localized news or enter keywords for specific topics.

2. **Fetch News**:
   - The tool fetches news articles using the NewsAPI based on your preferences.

3. **Personalized Recommendations**:
   - NewsGenius analyzes your input and recommends articles aligned with your interests.

4. **Interactive Display**:
   - View headlines, summaries, and descriptions.
   - Access the full articles with a single click.

---

## Technologies Used

- **Programming Language**: Python
- **Framework**: Streamlit (for the web interface)
- **APIs**:
  - [NewsAPI](https://newsapi.org/) for fetching real-time news articles.
  - [OpenAI](https://platform.openai.com/) for potential advanced NLP features.
- **Libraries**:
  - `requests`: For API calls.
  - `scikit-learn`: For TF-IDF and cosine similarity.
  - `streamlit`: For building the user interface.
  - `nltk`: For text preprocessing.
  - `dotenv`: For securely managing API keys.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/NewsGenius.git
   cd NewsGenius
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv news_project_env
   source news_project_env/bin/activate  # On Windows: news_project_env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure API keys:
   - Create a `.env` file in the root directory.
   - Add your API keys:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key
     NEWS_API_KEY=your_newsapi_key
     ```

5. Run the application:
   ```bash
   streamlit run app.py
   ```

---

## Project Structure

```
NewsGenius/
├── src/
│   ├── NewsGenius/
│   │   ├── components/
│   │   │   ├── fetcher.py
│   │   │   ├── recommender.py
│   │   ├── utils/
│   │   │   ├── news_fetcher.py
│   │   │   ├── personalization.py
│   │   ├── logging/
│   │   │   ├── __init__.py
│   │   ├── interface/
│   │   │   ├── interface.py
│   │   ├── config/
│   │   │   ├── configuration.py
│   │   │   ├── config.yaml
├── research/
│   ├── trials.ipynb
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
├── setup.py
```

---

## Future Enhancements

1. **Multilingual Support**:
   - Translate articles into different languages for a global audience.

2. **Sentiment Analysis**:
   - Analyze the tone of articles (positive, neutral, negative).

3. **Mobile Support**:
   - Make the interface mobile-friendly for on-the-go usage.

4. **Live News Feeds**:
   - Incorporate live news updates in real-time.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- Special thanks to [NewsAPI](https://newsapi.org/) for providing the news data.
- Gratitude to the [OpenAI](https://openai.com/) team for their exceptional APIs.

---
