import logging
import logging.handlers

def setup_logging():
    log_file = 'log.txt'
    formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setFormatter(formatter)

    # Set logging level and attach handlers to root logger
    logging.root.setLevel(logging.INFO)
    logging.root.addHandler(file_handler)

    # Close the file handler to ensure all log messages are written
    logging.shutdown()
    file_handler.close()