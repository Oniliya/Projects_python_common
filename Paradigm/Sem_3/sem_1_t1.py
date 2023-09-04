class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person1 = Person("Alice", 30)
person2 = Person("Bob", 25)        

print(person1.name) # Вывод: "Alice"
print(person2.age) # Вывод: 25

person1.greet() # Вывод: "Hello, my name is Alice and I am 30 years old."
person2.greet() # Вывод: "Hello, my name is Bob and I am 25 years old."



