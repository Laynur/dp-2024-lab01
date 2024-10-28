from lib.Logger import Logger
from lib.LevelMessage import LevelMessage
import threading


def worker(level: str, message: str):
    logger = Logger()
    print(logger)
    logger.log(level.value, message)


for i in range(10):
    th = threading.Thread(target=worker, args=(LevelMessage.INFO, f'Поток {i}'))
    th.start()