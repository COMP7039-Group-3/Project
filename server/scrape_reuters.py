from scrape import scrape, scrapeAndSum
from saveToJson import to_file

root_url = "https://www.reuters.com/"
sections = ["finance", "news/world", "news/technology", "news/lifestyle"]


def scrape_reuters():
    global root_url, sections
    articles = scrapeAndSum(root_url, sections)
    return articles


def scrape_reuters_and_save():
    articles = scrape_reuters()
    to_file("reuters.json", articles)
    return articles


if __name__ == '__main__':
    scrape_reuters(root_url, sections)
