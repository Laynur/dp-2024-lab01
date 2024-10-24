from datetime import datetime
import threading
import os


class Logger:

    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if not hasattr(cls, 'instance'):
                cls.instance = super(Logger, cls).__new__(cls)
                cls.instance._create_log()
        return cls.instance

    """
        Метод для создания нового файла с логами
    """
    def _create_log(self):
        time_now = datetime.now().strftime('%Y-%m-%d.%H-%M-%S')
        log_file_name = f"DP.P1.{time_now}.log"
        self.log_file_path = os.path.join(os.getcwd(), log_file_name)

    """
        Метод записывающий собщения в файл
    """
    def record_log_to_file(self, level: str, message: str):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"{timestamp} [{level}] {message}\n"

        with self._lock:
            with open(self.log_file_path, 'a') as log_file:
                log_file.write(log_message)


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance