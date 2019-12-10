from scrape import scrape, scrapeAndSum
from saveToJson import to_file

root_url = "https://www.bbc.com"
sections = ["news/world", "news/business", "news/technology", "news/science_and_environment"]

def scrape_bbc_news(root_url, sections):
    articles = scrapeAndSum(root_url, sections)
    return articles

def scrape_bbc_newsAndSave(root_url, sections):
    articles = scrapeAndSum(root_url, sections)
    to_file("bbc.json", articles)

scrape_bbc_news(root_url, sections)
