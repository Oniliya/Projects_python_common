# императивное (описание шаг за шагом - последовательности действий)
def sum_imperative(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

result = sum_imperative(5)
print(result) # Вывод: 15



# декларативное (описание результата без описания процесса)
def sum_declarative(n):
    return sum(range(1, n+1))

result = sum_declarative(5)
print(result) # Вывод: 15


# -----------------------
class Parent:
    def speak(self):
        print("Hello from Parent")

class Child(Parent):
    def speak(self):
        print("Hello from Child")

parent = Parent()
child = Child()

parent.speak() # Вывод: "Hello from Parent"
child.speak() # Вывод: "Hello from Child"