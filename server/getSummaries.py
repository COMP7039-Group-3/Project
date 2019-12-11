import requests
from bs4 import BeautifulSoup
from summarizer import summarize
from saveToJson import to_file

# Definitions #


class Article:
    def __init__(self, url, title, text):
        self.url = url
        self.title = title
        self.text = text

    def text_wordcount(self):
        return self.text.split(" ")

    def toJSON(self):
        return {"url": self.url, "title": self.title, "text": self.text}


class ArticleWithSum:
    def __init__(self, url, title, text, summary):
        self.url = url
        self.title = title
        self.text = text
        self.summary = summary

    def text_wordcount(self):
        return self.text.split(" ")

    def text_wordcount(self):
        return self.summary.split(" ")

    def toJSON(self):
        return {"url": self.url, "title": self.title, "text": self.text, "summary": self.summary}

# Functionality #

#
# Params:
# (String)      Origin URL - url of the news page
# (Soup-type)   HTML of the content to analyse
# Returns:
# Valid input   String with page content
# Invalid input None
#


def get_article_title(url, soup, debug=False):
    if ("bbc.com" in url
            or "bbc.co.uk" in url):
        if(debug):
            print("Found bbc domain")
            print(f"DEBUG: {soup.find('h2', {'class': 'unit__title'})}")

        tag = soup.find("h1", {"class": "story-body__h1"})
        # Blogs look different
        if tag is None:
            if(debug):
                print("Trying blog pattern")
            tag = soup.find("h2", {"class": "unit__title"}).find("span")
        # Media pages look different
        if tag is None:
            if(debug):
                print("Trying media page pattern")
            tag = soup.find("h1", {"class": "vxp-media__headline"})
        # More weird blogs // fallback
        if tag is None:
            tag = soup.find("h1")
        title = tag.text

    if ("theguardian.com" in url):
        if(debug):
            print("Found guardian domain")
        tag = soup.find("h1", {"itemprop": "headline"})
        title = tag.text

    if ("reuters.com" in url):
        if(debug):
            print("Found reuters domain")
        tag = soup.find("h1", {"class": "ArticleHeader_headline"})
        if tag is None:
            tag = soup.find("h2", {"class": "FeedItemHeadline_headline"})
        title = tag.text
    # returns None if title is not assigned
    # https://stackoverflow.com/a/15300733

    if(debug):
        print(f"DEBUG: Title : {tag}")

    return title

#
# Params:
# (String)      Origin URL - url of the news page
# (Soup-type)   HTML of the content to analyse
# Returns:
# Valid input   String with article content
# Invalid input None
#


def get_article_content(url, soup, debug=False):
    # Please don't ask me why this is now different than before
    article = None

    if(debug):
        print(url)

    if ("bbc.com" in url
            or "bbc.co.uk" in url):
        if(debug):
            print("Found bbc domain")
        new_body = soup.find("div", {"property": "articleBody"})
        # Media pages look different
        if new_body is None:
            new_body = soup.find("div", {"class": "vxp-media__summary"})

    if ("theguardian.com" in url):
        if(debug):
            print("Found guardian domain")
        new_body = soup.find("div", {"itemprop": "articleBody"})
        if new_body is None:
            new_body = soup.find("div", {"class": "content__article-body"})
        if new_body is None:
            new_body = soup.find("div", {"data-component": "standfirst"})

    if ("reuters.com" in url):
        if(debug):
            print("Found reuters domain")
        new_body = soup.find("div", {"class": "StandardArticleBody_body"})
        if new_body is None:
            new_body = soup.find("p", {"class": "FeedItemLede_lede"})

    paragraphs = new_body.findAll("p")
    for paragraph in paragraphs:
        if article is None:
            article = ""
        article = article + paragraph.text + "\n"
    return article

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


def get_article_url_list(url, count=5, debug=False):
    soup = http_get_soup(url)
    # Sets will ensure all urls are unique
    urls = set()
    root_url = identify_root_url(url, debug)

    if ("bbc.com" in url):
        bodies = soup.findAll("div", {"class": "gs-c-promo-body"})
    if ("theguardian.com" in url):
        bodies = soup.findAll("div", {"class": "fc-item__container"})
    if ("reuters.com" in url):
        bodies = soup.findAll("article", {"class": "story"})
    # Add Washington Post here

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
# Valid input   List of articles in JSON format
#


def get_articles_from_section(section_url, debug=False):
    url_list = get_article_url_list(section_url)
    articles = []

    for url in url_list:
        article = get_article(url).toJSON()
        if article is not None:
            articles.append(article)
    return articles


def get_articles_from_section_w_sum(section_url, debug=False):
    url_list = get_article_url_list(section_url)
    articles = []

    for url in url_list:
        article = get_article(url)
        summary = summary_from_article(article).toJSON()
        if summary is not None:
            articles.append(summary)
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
def get_article(url, debug=False):
    html = http_get_soup(url)

    if(debug):
        # print(html)
        print(url)

    title = get_article_title(url, html, debug)
    text = get_article_content(url, html, debug)
    if(title == None):
        print(f"ERROR: could not get title of article @ URI {url}")
        return None
    if(text == None):
        print(f"ERROR: could not get text of article @ URI {url}")
        return None
    return Article(url, title, text)

#
# Uses smmry to create a short summary of an article
#
# Params:
# (Article)     Article object
# Returns:
# Valid input   Summary of the article as per smmry lib
# Invalid input None
#


def summary_from_article(article, debug=False):
    summary_text = ""
    if(debug):
        print(article.text)
    if(len(article.text) > 0):
        summary_text = summarize(article.title, article.text)
    return ArticleWithSum(article.url, article.title, article.text, summary_text)

# Utils


def http_get_soup(url):
    result = requests.get(url)
    return soup_from_html(result.content)


def soup_from_html(html):
    return BeautifulSoup(html, features="html.parser")


def identify_root_url(url, debug=False):
    if ("bbc.com" in url
            or "bbc.co.uk" in url):
        return "https://bbc.com"
    if ("theguardian.com" in url):
        return "https://theguardian.com"
    if ("reuters.com" in url):
        return "https://reuters.com"
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
    file_name = news_page + article.title
    to_file("file_name.json", article)


def save_article_w_summary_to_file(url, article):

    print("Save the following article" + str(article.title))

    summary = summary_from_article(article, True)
    summary_wordcount = len(summary.split())
    summed_article = {"url": url, "article": article,
                      "summary": summary, "summary_wordcount": summary_wordcount}

    news_page = identify_root_url(url)
    file_name = news_page + article.title + "_summarised"
    to_file("file_name.json", summed_article)
