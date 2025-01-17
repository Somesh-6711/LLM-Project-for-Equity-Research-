import logging
import os
from pathlib import Path

def setup_logging(log_level="INFO", log_format="[%(asctime)s]: %(message)s", log_file="logs/project.log"):
    """
    Sets up logging configuration for the project.
    """
    os.makedirs(Path(log_file).parent, exist_ok=True)

    logging.basicConfig(
        level=log_level,
        format=log_format,
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_file, mode='a'),
        ],
    )
    logging.info("Logging setup complete.")
