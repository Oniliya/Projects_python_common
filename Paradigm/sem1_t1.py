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

# -----------------------
def filter_even_imperative(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = filter_even_imperative(numbers)
print(even_numbers) # Вывод: [2, 4, 6, 8]


# -----------------------
def filter_even_declarative(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = filter_even_declarative(numbers)
print(even_numbers) # Вывод: [2, 4, 6, 8]


# -------------------------------
def sum_even_sq(my_list: list) -> int:
    result=0
    for num in my_list:
        if num%2==0: result+=num*num
    return result

print(sum_even_sq(numbers))


# ----------------------------
def sum_of_squares_declarative(numbers):
    return sum([num ** 2 for num in numbers if num % 2 == 0])

print(sum_of_squares_declarative(numbers))