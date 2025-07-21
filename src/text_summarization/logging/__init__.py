import logging
import os
import sys
from datetime import datetime

# LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d')}.log"
logging_str='[%(asctime)s: %(levelname)s: %(module)s: %(message)s]'
log_dir = "logs"
log_filepath = os.path.join(log_dir,'running_logs.log')
# log_filepath = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(log_dir, exist_ok=True)

# LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    format=logging_str,
    level=logging.INFO,
    handlers=[
        logging.FileHandler(log_filepath, mode='a'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("text_summarization_logger")
if __name__=="__main__":
    logger.info("Logging has started successfully.")