import streamlit as st
from openai import OpenAI
from config import OPENAI_API_KEY
# from newsapi import NewsApiClient
import os

# Initialize News API
# newsapi = NewsApiClient(api_key='YOUR_NEWSAPI_KEY')

# Function to fetch news
def fetch_news(topic):
    top_headlines = newsapi.get_top_headlines(q=topic, language='en')
    news_titles = [article['title'] for article in top_headlines['articles']]
    return ' '.join(news_titles)

# Function to generate a blog article
def generate_blog(topic):

    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key= st.secrets['OPEN_AI_KEY'] # OPENAI_API_KEY,
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"write a comprehensive blog topic about {topic}",
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content

# Streamlit app layout
st.title("Blog Article Generator")

# Input for topic
topic = st.text_input("Enter the topic for the blog article:")

if st.button("Generate Blog Article"):
    with st.spinner('Fetching news and generating article...'):
        # news_context = fetch_news(topic)
        blog_article = generate_blog(topic)
        st.write(blog_article)
