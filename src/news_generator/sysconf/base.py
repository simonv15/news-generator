# %%
import os, yaml, collections

def load_yaml_file(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
_module_filepath = os.path.dirname(os.path.abspath(__file__))
_secret_api_key_fp = os.path.join(_module_filepath, "secret_api_keys.yaml")
_secret_news_sources_fp = os.path.join(_module_filepath, "secret_news_sources.yaml")

api_key_dict = load_yaml_file(_secret_api_key_fp).get('api_key_dict', {})
news_source_list = load_yaml_file(_secret_news_sources_fp).get('news_source_list', [])

conf = collections.OrderedDict()

conf["api_key_dict"] = api_key_dict
conf["news_source_list"] = news_source_list
# %%
