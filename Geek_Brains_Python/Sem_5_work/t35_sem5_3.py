# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


def check_simple(num: int) -> bool:
    k=2
    while k<=num//2:
        if num%k==0 :
            return False
        k+=1
    return True

def main():
    number=int(input("Введите число для проверки -> "))

    if check_simple(number):
        print("yes")
    else:
        print("no")



main()