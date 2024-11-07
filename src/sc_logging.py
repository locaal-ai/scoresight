import logging
import os
from platformdirs import user_log_dir
from datetime import datetime
from dotenv import load_dotenv

from resource_path import resource_path


def setup_logging():
    # Load the environment variables from the .env file
    load_dotenv(resource_path(".env"))

    # Create a logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # get the user data directory
    data_dir = user_log_dir("scoresight")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # basic config - send all logs to a file with UTF-8 encoding
    logging.basicConfig(
        filename=os.path.join(data_dir, f"scoresight_std_{current_time}.log"),
        level=logging.INFO,
        encoding="utf-8",  # Add explicit UTF-8 encoding
        errors="replace",  # Replace invalid characters instead of crashing
    )

    # prepend the user data directory
    log_file_path = os.path.join(data_dir, f"scoresight_{current_time}.log")

    # Create a file handler with UTF-8 encoding
    file_handler = logging.FileHandler(
        log_file_path,
        encoding="utf-8",  # Add explicit UTF-8 encoding
        errors="replace",  # Replace invalid characters instead of crashing
    )
    file_handler.setLevel(logging.DEBUG)

    # Create a formatter that can handle Unicode
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(module)s - %(message)s"
    )
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

    return logger, file_handler, log_file_path


try:
    # Create a logger
    logger, file_handler, log_file_path = setup_logging()
except Exception as e:
    print(f"Error setting up logging: {e}")
