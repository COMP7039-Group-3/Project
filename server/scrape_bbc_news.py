from getSummaries import get_summaries
from saveToJson import save_to_json, empty_summaries_folder

#####################################################################################


def scrape_bbc_news(summaries_per_section=5, summarize_to_lines=3, save=True):

    urls_list = []

    root_url = "https://www.bbc.com"
    sections = ["news/world", "news/business",
                "news/technology", "news/science_and_environment"]
    # sections = ["news/world", "news/business"]

    num_sections = 0
    num_summaries = 0

    #####################################################################################

    empty_summaries_folder()

    for section in sections:
        urls = get_summaries(
            root_url, section, summaries_per_section, summarize_to_lines)

        if (save):
            save_to_json(urls, section)
        num_sections += 1
        num_summaries += len(urls)
        print(f"{section}: {str(len(urls))} articles summarized.")
        urls_list.append({"section": section, "urls": urls})

    print(
        f"\n✅  Summarized {num_summaries} articles in {num_sections} sections.\n")

    save_to_json(urls_list, "news")
    return urls_list
