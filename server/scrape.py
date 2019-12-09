from getSummaries import get_articles_from_section

def scrape(root_url, sections, summaries_per_section=5, summarize_to_lines=3, save=True):
    num_sections = 0
    num_summaries = 0
    scraped_page_articles = []

    for section in sections:
        constructed_url = root_url + "/" + section
        articles = get_articles_from_section(constructed_url)
        
        num_sections += 1
        num_summaries = len(articles)
        print(f"INFO: {section}: {str(num_summaries)} articles summarized.")
        scraped_page_articles.append({"section": section, "articles": articles})

    print(f"\n✅  Summarized {num_summaries} articles in {num_sections} sections.\n")

    return scraped_page_articles