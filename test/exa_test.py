from exa_py import Exa
import os
from dotenv import load_dotenv

load_dotenv()


def get_competitor_urls(url: str = None, description: str = None) -> list:
    """
    Fetch up to 5 competitor URLs using Exa AI based on a company URL or description.
    """

    exa = Exa(os.getenv("EXA_API_KEY"))

    if url:
        result = exa.find_similar(
            url=url, num_results=5, exclude_source_domain=True, category="company"
        )
    else:
        result = exa.search(
            query=description,
            type="neural",
            category="company",
            use_autoprompt=True,
            num_results=5,
        )

    urls = [item.url for item in result.results]
    return urls
