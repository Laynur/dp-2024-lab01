from datetime import datetime
from lib.LevelMessage import LevelMessage
import threading
import os


class Logger:
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if not hasattr(cls, 'instance'):
                cls.instance = super(Logger, cls).__new__(cls)
                cls.instance._create_file_path()
        return cls.instance

    def _create_file_path(self):
        """
        Метод для создания нового файла с логами
        """
        time_now = datetime.now().strftime('%Y-%m-%d.%H-%M-%S')
        log_file_name = f"DP.P1.{time_now}.log"
        self.log_file_path = os.path.join(os.getcwd(), log_file_name)

    def log(self, level: str, message: str):
        """
        Метод записывающий собщения в файл
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"{timestamp} [{level}] {message}\n"

        with self._lock:
            with open(self.log_file_path, 'a') as log_file:
                log_file.write(log_message)
