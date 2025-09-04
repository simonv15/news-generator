# %%
import sys, os, collections

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.news_generator.scraper.base import scrape_content
from src.news_generator.utils.base import logger, log_traceback
from src.news_generator.sysconf.base import conf


# %%
test_url_list = [source['url'] for source in conf['news_source_list'] if source.get('enable', False)]
test_url_list
# %%
formats = ['markdown', 'html']
actions = [
    {"type": "scroll", "direction": "down"},
    {"type": "wait", "milliseconds": 3000}
]
scrape_result = scrape_content(test_url_list[0], formats, actions)
# %%
