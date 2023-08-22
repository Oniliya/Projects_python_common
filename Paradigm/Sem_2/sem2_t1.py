# def greet(name):
#     print("Здравствуйте,")
#     print(name)
#     print("Как вы себя чувствуете сегодня?")


# def rate_movie(score):
#     if score > 8:
#         return "Отличный фильм!"
#     elif score > 6:
#         return "Хороший фильм."
#     else:
#         return "Средний или плохой фильм."

# print(rate_movie(9))

# def sum_to_n(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#         return total

# print(sum_to_n(100))

def say_hello(): # Это подпрограмма
    print("Привет!")

def show_message(message): # Это процедура
    print(message)

show_message("Это сообщение.")

def add(a, b): # Это функция
    return a + b

result = add(3, 4)
print(result)

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self): # Это метод
        print(f"{self.name} говорит: Гав!")

dog = Dog("Бобик")
dog.bark()


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Тестирование функции
if __name__ == "__main__":

    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный массив:", test_array)

    bubble_sort(test_array)
    print("Отсортированный массив:", test_array)



def factorial(n):
    if n <= 1:
        return 1
    else:
        result = 1
    for i in range(2, n + 1):
        result *= i
        return result

number = 5
print(f"Факториал {number} = {factorial(number)}")


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = 10
print(f"{number}-е число Фибоначчи = {fibonacci(number)}")


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = 56
num2 = 98
print(f"НОД({num1}, {num2}) = {gcd(num1, num2)}")


def fast_pow(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 1:
        return fast_pow(base, exponent - 1) * base
    else:
        half_pow = fast_pow(base, exponent // 2)
        return half_pow * half_pow

base = 2
exponent = 10
print(f"{base} в степени {exponent} = {fast_pow(base, exponent)}")



# public class DayOfWeek {

# public String getDay(int dayNumber) {
# String day;
# switch(dayNumber) {
# case 1:
# day = "Monday";
# break;
# case 2:
# day = "Tuesday";
# break;
# case 3:
# day = "Wednesday";
# break;
# case 4:
# day = "Thursday";
# break;
# case 5:
# day = "Friday";
# break;
# case 6:
# day = "Saturday";
# break;
# case 7:
# day = "Sunday";
# break;
# default:
# day = "Invalid day number";
# }
# return day;
# }

# public static void main(String[] args) {
# DayOfWeek dayOfWeek = new DayOfWeek();
# System.out.println(dayOfWeek.getDay(5)); // Prints "Friday"
# }
# }