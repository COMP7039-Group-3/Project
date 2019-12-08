from getSummaries import get_articles_from_section, save_article_w_summary_to_file

#
# Scrapes BBC.com landing page
# Params: 
# (Number:optional)     Summary count per section, defaults to 5
# (Number:optional)     Length of summary, defaults to 3
# (Boolean:optional)    Creates JSON output in $project/summaries folder, defaults to false
#                       Should only be used for debugging

def scrape_bbc_news(summaries_per_section=5, summarize_to_lines=3, save=False):
    root_url = "https://www.bbc.com"
    sections = ["news/world", "news/business",
                "news/technology", "news/science_and_environment"]

    num_sections = 0
    num_summaries = 0
    scraped_page_articles = []

    for section in sections:
        constructed_url = root_url + "/" + section
        articles = get_articles_from_section(constructed_url)
        
        num_sections += 1
        num_summaries = len(articles)
        print(f"{section}: {str(num_summaries)} articles summarized.")
        scraped_page_articles.append({"section": section, "articles": articles})

    print(f"\n✅  Summarized {num_summaries} articles in {num_sections} sections.\n")

    return scraped_page_articles

def scrape_bbc_news_and_save():
    root_url = "https://www.bbc.com"
    sections = ["news/world", "news/business",
                "news/technology", "news/science_and_environment"]

    for section in sections:
        constructed_url = root_url + "/" + section
        articles = get_articles_from_section(constructed_url)
        for article in articles:
            save_article_w_summary_to_file(constructed_url, article)

scrape_bbc_news_and_save()