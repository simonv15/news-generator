import sys, os, collections

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.news_generator.data_mnmt.base import save_pickle_data, load_pickle_data

options = {
    'run_date': '2025-08-27'
}

data = collections.OrderedDict({
    'title': 'Sample News',
    'content': 'This is a sample news content.',
    'author': 'John Doe'
})
save_pickle_data(data, options)

loaded_data = load_pickle_data(options)
for k, v in loaded_data.items():
    print(f"{k}: {v}")