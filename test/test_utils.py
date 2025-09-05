# %% import
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.news_generator.utils.base import logger, log_traceback
# %% test log_traceback
def test_log_traceback():
    try:
        # Deliberately cause a ZeroDivisionError
        result = 1 / 0
    except Exception as e:
        log_traceback(e)
test_log_traceback()
# %%
