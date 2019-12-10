from scrape import scrape, scrapeAndSum
from saveToJson import to_file

root_url = "https://www.washington-post.com/"
sections = ["finance", "news/world", "news/technology", "news/lifestyle"]


def scrape_washington():
    global root_url, sections
    articles = scrape(root_url, sections)
    return articles


def scrape_washington_and_save():
    articles = scrape_washington()
    to_file("washington.json", articles)
    return articles
