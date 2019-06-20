import logging
import os


def create_logger(path):
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler(os.path.join(path, "log.txt"))
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(asctime)s %(name)s:%(lineno)d][%(levelname)s] %(message)s')
    handler.setFormatter(formatter)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    logger.addHandler(handler)
    logger.addHandler(console)

    return logger


if __name__ == '__main__':
    logger = create_logger('../test/')
    logger.info('starting training')
