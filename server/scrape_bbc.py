from scrape import scrape, scrapeAndSum
from saveToJson import to_file

root_url = "https://www.bbc.com"
sections = ["news/world", "news/business",
            "news/technology", "news/science_and_environment"]


def scrape_bbc():
    global root_url, sections
    articles = scrapeAndSum(root_url, sections)
    return articles


def scrape_bbc_and_save():
    articles = scrape_bbc()
    to_file("bbc.json", articles)
    return articles
