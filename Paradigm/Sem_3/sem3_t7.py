class Observer:
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def update(self, message):
        print("Received message:", message)

class Subject:
    _observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

# Создаем экземпляр наблюдаемого объекта (подлежащего изменениям)
subject = Subject()

# Создаем экземпляры наблюдателей
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

# Присоединяем наблюдателей к наблюдаемому объекту
subject.attach(observer1)
subject.attach(observer2)

# Уведомляем наблюдателей о событии
subject.notify("Hello, observers!") # Вывод: "Received message: Hello, observers!"