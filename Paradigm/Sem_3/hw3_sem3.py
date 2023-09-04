# На Выбор Часть 1 или Часть 2

# Часть 1: Парадигмы программирования и ООП
# __

# __
# Шаблон Singleton:
# Реализуйте паттерн Singleton на языке Python для класса Logger, который будет использоваться для логирования информации в приложении. 
# Гарантируйте, что только один экземпляр класса Logger будет создан.
# __



class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance
 
class Logger(Singleton):
    pass