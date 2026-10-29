import logging
import os
import sys

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT = "[%(asctime)s] %(name)s %(levelname)s - %(message)s"


def config_root_logger() -> logging.Logger:
    root_logger = logging.getLogger("fuzzy_fs")
    root_logger.setLevel(LOG_LEVEL)
    if not root_logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(LOG_LEVEL)
        handler.setFormatter(logging.Formatter(LOG_FORMAT))
        root_logger.addHandler(handler)
    return root_logger


logger = config_root_logger()
