from lib.Logger import Logger, Singleton
import threading
log = Logger()
log1 = Logger()
print(log)
print(log1)

# s = Singleton()
# print(s.instance)
# print("Создан объект",s)
# s1 = Singleton()
# print("Создан объект",s1)