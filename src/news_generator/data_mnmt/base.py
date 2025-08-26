import os
import pickle

from ..sysconf.base import conf

def save_pickle_data(data, options):
    date = options.get('run_date')
    folder = os.path.join(conf["data_folder_path"], date)
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, "data.pkl")
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)

def load_pickle_data(options):
    date = options.get('run_date')
    folder = os.path.join(conf["data_folder_path"], date)
    file_path = os.path.join(folder, "data.pkl")
    with open(file_path, 'rb') as f:
        return pickle.load(f)