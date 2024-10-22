

class Logger:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Logger, cls).__new__(cls)
        return cls.instance

    """
    Метод записывающий собщения в файл
    """
    def record_to_file(self):
        pass
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