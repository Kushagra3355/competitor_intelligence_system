from firecrawl import FirecrawlApp
import os
import json
from dotenv import load_dotenv

load_dotenv()


def scrape_website(url: str):

    app = FirecrawlApp(os.getenv("FIRECRAWL_API_KEY"))

    extraction_prompt = """
            Extract detailed information about the company's offerings, including:
            - Company name and basic information
            - Pricing details, plans, and tiers
            - Key features and main capabilities
            - Technology stack and technical details
            - Marketing focus and target audience
            - Customer feedback and testimonials

            Use the full website content for your answer.
        """

    print(f"Scraping {url}...")
    result = app.extract([url], prompt=extraction_prompt)

    print(f"\n✓ Successfully scraped {url}")
    return result


if __name__ == "__main__":

    result = scrape_website("https://www.langchain.com/")

    print("SCRAPING RESULTS")

    if "markdown" in result:
        print("\nMarkdown Content (first 500 chars):")
        print("-" * 50)
        print(result["markdown"][:500] + "...")

    if "metadata" in result:
        print("\n\nMetadata:")
        print("-" * 50)
        print(json.dumps(result["metadata"], indent=2))

    output_file = "scraped_content.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"\n✓ Full content saved to {output_file}")
