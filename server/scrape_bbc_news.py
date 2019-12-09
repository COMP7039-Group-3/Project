from scrape import scrape
from saveToJson import to_file

root_url = "https://www.bbc.com"
sections = ["news/world", "news/business", "news/technology", "news/science_and_environment"]

def scrape_bbc_news(root_url, sections):
    articles = scrape(root_url, sections)
    to_file("bbc.json", articles, True)

scrape_bbc_news(root_url, sections)
