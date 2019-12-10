from scrape import scrape, scrapeAndSum
from saveToJson import to_file

root_url = "https://www.reuters.com/"
sections = ["finance", "news/world", "news/technology", "news/lifestyle"]

def scrape_reuters_news(root_url, sections):
    articles = scrape(root_url, sections)
    to_file("reuters.json", articles)

scrape_reuters_news(root_url, sections)
