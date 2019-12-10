from getSummaries import get_articles_from_section, get_articles_from_section_w_sum

def scrape(root_url, sections):
    num_sections = 0
    num_articles = 0
    scraped_page_articles = []

    for section in sections:
        constructed_url = root_url + "/" + section
        articles = get_articles_from_section(constructed_url)
        
        num_sections += 1
        num_articles = len(articles)
        scraped_page_articles.append({"section": section, "articles": articles})

    print(f"\n✅  Collected {num_articles} articles in {num_sections} sections.\n")

    return scraped_page_articles

def scrapeAndSum(root_url, sections, summaries_per_section=5, summarize_to_lines=3):
    num_sections = 0
    num_articles = 0
    scraped_page_articles = []

    for section in sections:
        constructed_url = root_url + "/" + section
        articles = get_articles_from_section_w_sum(constructed_url)

        num_sections += 1
        num_articles = len(articles)
        print(f"INFO: {section}: {str(num_articles)} articles summarized")
        scraped_page_articles.append({"section": section, "articles": articles})

    print(f"\n✅  Summarized {num_articles} articles in {num_sections} sections.\n")

    return scraped_page_articles