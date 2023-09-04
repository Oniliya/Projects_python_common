# На Выбор Часть 1 или Часть 2

# Часть 1: Парадигмы программирования и ООП

# ООП Концепции:
# Создайте класс Person, который имеет атрибуты name, age и метод introduce(), выводящий информацию о человеке. 
# Создайте несколько объектов этого класса и вызовите метод introduce() для каждого из них.
# __


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        self.intro = self.name+" - "+str(self.age)
        return self.intro
    
man1 = Person("Tom", 19)
man2 = Person("Bill", 29)
man3 = Person("Anna", 21)

print(man1.introduce())
print(man2.introduce())
print(man3.introduce())