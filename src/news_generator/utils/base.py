import logging, traceback

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def log_traceback(e):
    logger.error("An error occurred: %s", e)
    logger.debug(traceback.format_exc())