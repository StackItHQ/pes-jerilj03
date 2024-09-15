# import logging

# def setup_logger():
#     logging.basicConfig(filename='sync.log', level=logging.INFO, format='%(asctime)s %(message)s')

# def log_sync(message):
#     logging.info(message)

import datetime
import logging

logging.basicConfig(filename='sync.log', level=logging.INFO)

def log_sync(message):
    logging.info(f"{datetime.datetime.now()}: {message}")
