import requests
from bs4 import BeautifulSoup
from summarizer import summarize


def get_bbc_article(url):
    return_text = ""
    new_result = requests.get(url)
    new_src = new_result.content
    new_soup = BeautifulSoup(new_src, features="html.parser")
    new_body = new_soup.find("div", {"property": "articleBody"})
    paragraphs = new_body.findAll("p")
    for paragraph in paragraphs:
        return_text = return_text + paragraph.text + "\n"
    return return_text


def get_summaries(root_url, section, count=5, summarize_to_lines=5):
    main_url = root_url + "/" + section
    result = requests.get(main_url)
    src = result.content
    soup = BeautifulSoup(src, features="html.parser")
    urls = []
    bodies = soup.findAll("div", {"class": "gs-c-promo-body"})
    bodies.pop(0)  # Repeated item

    print("\nGetting summaries for: " + section + " ...")
    for body in bodies[:count]:
        title = body.find("h3").text
        text = body.find("p")
        link = body.find("a")
        url = link.attrs['href']
        try:
            if (url.startswith("/")):
                url = root_url + url

            found = next((x for x in urls if x['url'] == url), None)
            if (found != None):
                print(f"  ❌  Url already processed: {url}")
            else:
                article_body = get_bbc_article(url)
                summary = "\n".join(
                    summarize(title, article_body, summarize_to_lines))
                article_words = len(article_body.split())
                summary_words = len(summary.split())
                urls.append({"url": url, "title": title, "summary": summary, "article": article_body,
                             "article_words": article_words, "summary_words": summary_words})
                print(f"  ✅  Got summary for article: {url}")
        except:
            print(f" 💀  Failed on url: {url}")
            pass

    return urls
