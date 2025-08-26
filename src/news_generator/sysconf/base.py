# %%
import os, yaml, collections
from pathlib import Path

def load_yaml_file(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

conf = collections.OrderedDict()

conf["_glb_prj_path"] = Path(__file__).resolve().parents[3].as_posix()

_sysconf_fp = os.path.join(conf["_glb_prj_path"], "src", "news_generator", "sysconf")
_secret_api_key_fp = os.path.join(_sysconf_fp, "secret_api_keys.yaml")
_secret_news_sources_fp = os.path.join(_sysconf_fp, "secret_news_sources.yaml")

api_key_dict = load_yaml_file(_secret_api_key_fp).get('api_key_dict', {})
news_source_list = load_yaml_file(_secret_news_sources_fp).get('news_source_list', [])


conf["api_key_dict"] = api_key_dict
conf["news_source_list"] = news_source_list

conf["data_folder_path"] = os.path.join(conf["_glb_prj_path"], "data")

# %%
