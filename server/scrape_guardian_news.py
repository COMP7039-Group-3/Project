from scrape import scrape, scrapeAndSum
from saveToJson import to_file

root_url = "https://www.theguardian.com"
sections = ["world", "uk/business", "uk/technology", "science"]

def scrape_guardian_news(root_url, sections):
    articles = scrapeAndSum(root_url, sections)
    to_file("theguardian.json", articles)

if __name__ == '__main__':
    scrape_guardian_news(root_url, sections)
