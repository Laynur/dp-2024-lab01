from lib.Logger import Logger, Singleton
import threading
log = Logger()
log.record_to_file("INFO", "Приложение запущено")

# s = Singleton()
# print(s.instance)
# print("Создан объект",s)
# s1 = Singleton()
# print("Создан объект",s1)