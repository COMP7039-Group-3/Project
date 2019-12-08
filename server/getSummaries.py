import requests
from bs4 import BeautifulSoup
from summarizer import summarize

# Functionality

# 
# Params:
# (String)      Origin URL - url of the news page
# (Soup-type)   HTML of the content to analyse
# Returns:
# Valid input   String with article content
# Invalid input None
#
def get_article_title(url, soup):
    if ("bbc.com" in url
    or "bbc.co.uk" in url):
        title = soup.find("h3", {"property": "articleBody"})
    if ("theguardian.com" in url):
        title = soup.find("h1", {"itemprop": "articleBody"})

    # returns None if title is not assigned
    # https://stackoverflow.com/a/15300733
    return title 

# 
# Params:
# (String)      Origin URL - url of the news page
# (Soup-type)   HTML of the content to analyse
# Returns:
# Valid input   String with article content
# Invalid input None
#
def get_article_content(url, soup):
    article = ""
    
    if ("bbc.com" in url
    or "bbc.co.uk" in url):
        new_body = soup.find("div", {"property": "articleBody"})
    if ("theguardian.com" in url):
        new_body = soup.find("div", {"itemprop": "articleBody"})
    
    paragraphs = new_body.findAll("p")
    for paragraph in paragraphs:
        article = article + paragraph.text + "\n"

    if(len(article) > 0):
        return article
    return None

# 
# Params:
# (Soup-type)   HTML of the content to analyse
# Returns:
# Valid input   String with link reference
# Invalid input None
#
def get_article_link(soup):
    link = soup.find("a")
    return link.attrs['href']

# 
# Params:
# (String)          Origin URL - url of the news page
# (Number:Optional) Number of links to capture
# Returns:
# Valid input       List of urls
#
def get_article_url_list(url, count=5):
    soup = http_get_soup(url)
    # Sets will ensure all urls are unique
    urls = set()
    root_url = identify_root_url(url)

    if ("bbc.com" in url):
        bodies = soup.findAll("div", {"class": "gs-c-promo-body"})
    if ("theguardian.com" in url):
        bodies = soup.findAll("div", {"class": "fc-item__container"})
    if(bodies):
        bodies.pop(0)  # Repeated item

    for body in bodies[:count]:
        url = get_article_link(body)
        
        # fix URI which might have relative reference
        # <a href="/new-uri">
        # <a href="./new-uri">
        if (url.startswith("/") or url.startswith("./")):
            url = root_url + "/" + url
        
        urls.add(url)
    return urls

#
# Visits a section, finds list of links and obtains
# article content 
#
# Params:
# (String)      URL - url of the news page
# Returns:
# Valid input   List of articles
#
def get_articles_from_section(section_url):
    url_list = get_article_url_list(section_url)
    articles = []

    for url in url_list:
        articles.append(get_article(url))
    return articles

#
# Visits an article page, obtains
# - article title 
# - article content 
#
# Params:
# (String)      URL - url of the news page
# Returns:
# Valid input   article
#    
def get_article(url):
    html = http_get_soup(url)
    title = get_article_title(url, html)
    text = get_article_content(url, html)
    result = { "title": title, "article": text, "url": url }
    return result

#
# Uses smmry to create a short summary of an article
#
# Params:
# (Article)     Article object
# Returns:
# Valid input   Summary of the article as per smmry lib
# Invalid input None
#    
def summary_from_article(article):
    title = article[title]
    text = article[text]
        
    if(len(text) > 0):
        return "\n".join(summarize(title, text, len(text)))
    return None

#
# Uses smmry to create a short summary of an article
#
# Params:
# (String)      Origin URL - url of the news page
# (Article)     Article object
# Returns:
# None; instead outputs file
#    
def save_article_to_file(url, article):
    news_page = identify_root_url(url)
    title = article[title]
    file_name = news_page + title
    to_file("file_name.json", article)
    return

def save_article_w_summary_to_file(url, article):
    summary = summary_from_article(article)
    summary_wordcount = len(summary.split())
    summed_article = { "url": url, "article": article, "summary": summary, "summary_wordcount": summary_wordcount }

    news_page = identify_root_url(url)
    title = article[title]
    file_name = news_page + title + "_summarised"
    to_file("file_name.json", summed_article)
    return

# Utils
def http_get_soup(url):
    result = requests.get(url)
    return soup_from_html(result.content)

def soup_from_html(html):
    return BeautifulSoup(html, features="html.parser")

def identify_root_url(url):
    if ("bbc.com" in url
    or "bbc.co.uk" in url):
        return "https://bbc.com"
    if ("theguardian.com" in url):
        return "https://theguardian.com"
    return None

def to_file(target_location, text):
    with open(target_location, "w") as file:
        file.write(text)
        file.close()