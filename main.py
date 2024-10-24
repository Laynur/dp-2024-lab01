from lib.Logger import Logger, Singleton
import threading


def worker(level: str, message: str):
    log = Logger()
    print(log)
    log.record_log_to_file(level, message)


for i in range(10000):
    th = threading.Thread(worker('INFO',f'Поток {i}'))
    th.start()