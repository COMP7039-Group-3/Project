from scrape import scrape
from saveToJson import to_file

root_url = "https://www.theguardian.com"
sections = ["world", "uk/business", "uk/technology", "science"]

def scrape_guardian_news(root_url, sections):
    articles = scrape(root_url, sections)
    to_file("summaries/theguardian.json", articles)

scrape_guardian_news(root_url, sections)
