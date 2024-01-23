from newsapi import NewsApiClient
import newsapi 

# Get your API key from News API


# Initialize the client
client = newsapi.NewsApiClient('dcd00510f4734ca680f217c72f668c80')

# Get top headlines
top_headlines = client.get_top_headlines(q="stock",
    category="business",
    language="en",
)


# Print the headlines
for article in top_headlines["articles"]:
    print(article["title"])