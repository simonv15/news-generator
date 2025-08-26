import os, yaml, collections

def load_yaml_file(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
_module_filepath = os.path.dirname(os.path.abspath(__file__))
_secret_filepath = os.path.join(_module_filepath, '__secret.yaml')

api_key_list = load_yaml_file(_secret_filepath).get('api_key_list', [])

conf = collections.OrderedDict()

conf["api_key_list"] = api_key_list