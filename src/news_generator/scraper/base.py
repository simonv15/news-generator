import os, sys

from firecrawl import FirecrawlApp

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sysconf.base import conf

def scrape_content(url, formats, actions):
    app = FirecrawlApp(api_key=conf["api_key_dict"].get("FIRECRAWL_API_KEY"))
    try:
        scrape_result = app.scrape(
            url=url,
            formats=formats,
            proxy="auto",
            actions=actions
        )
        if scrape_result:
            return scrape_result
    except Exception as e:
        print(f" {url}: {e}")

def get_news_urls():
    pass

def get_news_content():
    pass