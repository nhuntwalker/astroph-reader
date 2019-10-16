import requests
from bs4 import BeautifulSoup as soup

from check_lexicon import make_readable, remove_latex_fmt

ASTROPH_URL = "https://arxiv.org/list/astro-ph/new"

response = requests.get(ASTROPH_URL)
response = requests.get(ASTROPH_URL)
html = soup(response.content, "html.parser")

new_articles = html.dl.find_all('dd')

formatted_articles = []

for article in new_articles:
    title = article.find(
        'div',
        attrs={'class': 'list-title'}
    ).text.strip().replace('Title: ', '')
    
    abstract = article.find(
        'p',
        attrs={'class': 'mathjax'}
    ).text.strip().replace('\n', ' ')

    formatted_article = {
        "title": title,
        "abstract": abstract
    }
    formatted_articles.append(formatted_article)

print(
    make_readable(
        remove_latex_fmt(formatted_articles[0]["abstract"])
    )
)
