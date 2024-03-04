"""Logger utility."""

import logging


def get_logger(logger_name, file=False, console=True):
    """Get logger for the calling module."""
    # Create a logger
    logger = logging.getLogger(logger_name)

    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        # Create a formatter and set it to the handler
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # Create a file handler
        if file is True:
            file_handler = logging.FileHandler("project.log")
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        if console is True:
            # Create a stream handler for logging to console
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

    return logger
