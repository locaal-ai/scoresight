import logging
import os
from platformdirs import user_log_dir
from datetime import datetime
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv(os.path.abspath(os.path.join(os.path.dirname(__file__), ".env")))

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# get the user data directory
data_dir = user_log_dir("scoresight")
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# basic config - send all logs to a file
logging.basicConfig(
    filename=os.path.join(data_dir, f"scoresight_std_{current_time}.log"),
    level=logging.INFO,
)

# prepend the user data directory
log_file_path = os.path.join(data_dir, f"scoresight_{current_time}.log")

# Create a file handler
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.DEBUG)

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# if the .env file has a debug flag, set the logger to output to console
if os.getenv("SCORESIGHT_DEBUG"):
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.debug("Debug mode enabled")

# check to see if there are more log files, and only keep the most recent 10
log_files = [
    f
    for f in os.listdir(data_dir)
    if f.startswith("scoresight_") and f.endswith(".log")
]
# sort log files by date
log_files.sort()
if len(log_files) > 10:
    for f in log_files[:-10]:
        try:
            os.remove(os.path.join(data_dir, f))
        except PermissionError as e:
            logger.error(f"Failed to remove log file: {f}")
