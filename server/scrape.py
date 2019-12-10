from getSummaries import get_articles_from_section, get_articles_from_section_w_sum


def scrape(root_url, sections):
    scraped_page_articles = []

    for section in sections:
        constructed_url = root_url + "/" + section
        articles = get_articles_from_section(constructed_url)

        scraped_page_articles.append(
            {"section": section, "articles": articles})

    print(
        f"\n✅  {root_url}: Collected {len(articles)} articles in {len(sections)} sections.\n")

    return scraped_page_articles


def scrapeAndSum(root_url, sections, summaries_per_section=5, summarize_to_lines=3):
    scraped_page_articles = []

    for section in sections:
        constructed_url = root_url + "/" + section
        articles = get_articles_from_section_w_sum(constructed_url)

        print(f"INFO: {section}: {str(len(articles))} articles summarized")
        scraped_page_articles.append(
            {"section": section, "articles": articles})

    print(
        f"\n✅  {root_url}: Summarized {len(articles)} articles in {len(sections)} sections.\n")

    return scraped_page_articles
