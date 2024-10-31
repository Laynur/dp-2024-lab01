from datetime import datetime
from lib.LevelMessage import LevelMessage
import threading
import os


class Logger:
    _lock_write = threading.Lock()
    _lock_create = threading.Lock()

    def __init__(self):
        self._create_file_path()

    def __new__(cls):
        with cls._lock_create:
            if not hasattr(cls, 'instance'):
                cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance

    def _create_file_path(self):
        """Метод для создания пути к файлу журнала"""
        time_now = datetime.now().strftime('%Y-%m-%d.%H-%M-%S')
        log_file_name = f"DP.P1.{time_now}.log"
        self.log_file_path = os.path.join(os.getcwd(), log_file_name)

    def log(self, level: LevelMessage, message: str):
        """Метод записывающий собщения в файл"""

        with self._lock_write:
            log_message = self._create_message(message=message, level=level)
            with open(self.log_file_path, 'a') as log_file:
                log_file.write(log_message)

    def _create_message(self, message: str, level: LevelMessage):
        """Метод для формирования строки лога"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f"{timestamp} [{level}] {message}\n"
