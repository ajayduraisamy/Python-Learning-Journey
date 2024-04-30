# 05_logging_exercises.py
# Logging practice tasks

import logging

logging.basicConfig(
    filename="exercise.log",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

# 1. Log login attempts
users = ["Ajay", "Kumar", "Suri"]

for u in users:
    logging.info(f"User {u} attempted login")

# 2. Log errors for invalid data
data = ["12", "xz", "98", "hello"]

for d in data:
    try:
        num = int(d)
        logging.info(f"Valid number: {num}")
    except:
        logging.error(f"Invalid number: {d}")
