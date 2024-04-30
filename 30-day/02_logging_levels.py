# 02_logging_levels.py
# Logging levels demo

import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debugging details")
logging.info("Information message")
logging.warning("Warning!")
logging.error("Error occurred!")
logging.critical("Critical issue!")
