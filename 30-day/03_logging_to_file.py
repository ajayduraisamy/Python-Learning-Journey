# 03_logging_to_file.py
# Writing logs to a file

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("App started")
logging.info("User logged in")
logging.error("Sample error message")
