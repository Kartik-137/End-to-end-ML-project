import os
import sys
import logging

# Define logging string format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs" # Directory to store log files

# Define log file path
log_filepath = os.path.join(log_dir, "running_log.log")
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level = logging.INFO,  # information related log
    format = logging_str,
    handlers=[
        logging.FileHandler(log_filepath), # Creates log folder on the machine
        logging.StreamHandler(sys.stdout) # to log on the terminal as well
    ]
)

logger = logging.getLogger("red_wine_quality_prediction_logger")
