from datetime import datetime


class Logger:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
            cls.instance._create_log()
        return cls.instance

    """
        Метод для создания нового файла с логами
    """
    def _create_log(self):
        now = datetime.now()
        self.filename = now.strftime("DP.P1.%Y-%m-%d.%H-%M-%S.log")
        with open(self.filename, 'w'):
            pass

    """
      Метод записывающий собщения в файл
    """
    def record_to_file(self, level: str, message: str):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, 'a') as log_file:
            log_file.write(f"{now} [{level}] {message}\n")
    """
    Метод для очистки существующего log файла.
    """
    def clear_last_log(self):
        pass

class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance