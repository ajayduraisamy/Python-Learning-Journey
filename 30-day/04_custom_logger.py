# 04_custom_logger.py
# Creating a custom logger

import logging

logger = logging.getLogger("AjayLogger")
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("custom.log")
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("Custom logger started")
logger.debug("Debugging info here")
logger.error("Error in custom logger")
