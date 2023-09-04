# На Выбор Часть 1 или Часть 2

# Часть 1: Парадигмы программирования и ООП
# __


# Шаблон Наблюдатель:
# Реализуйте паттерн Наблюдатель на языке Python для системы уведомлений. Создайте класс NotificationSystem (наблюдаемый объект), 
# который будет иметь методы для добавления наблюдателей и уведомления о событиях. Создайте несколько наблюдателей, реагирующих на уведомления.
# 

from abc import ABC, abstractmethod


class NotificationSystem:
    def __init__(self):
        self.__observers = set()

    def add_observer(self, observer):
        self.__observers.add(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify(self):
        for observer in self.__observers:
            observer.make_notification()


class AbstractObserver(ABC):
    @abstractmethod
    def make_notification(self):  
        pass


class Observ(AbstractObserver):
    def __init__(self, name):
        self.name = name

    def make_notification(self):
        print('{} воспроизвел уведомление'.format(self.name))


# Создадим 3 наблюдателя.
obs1 = Observ('Наблюдатель #1')
obs2 = Observ('Наблюдатель #2')
obs3 = Observ('Наблюдатель #3')

# Создадим центральный пульт управления.
obs_system = NotificationSystem()

# Подключим все 3 наблюдателя.
obs_system.add_observer(obs1)
obs_system.add_observer(obs2)
obs_system.add_observer(obs3)

# Передаем им сообщения
obs_system.notify()

# Отключим одного из наблюдателей
obs_system.remove_observer(obs1)
print("--------------- первый наблюдатель отключен")

# Передаем им сообщения
obs_system.notify()

