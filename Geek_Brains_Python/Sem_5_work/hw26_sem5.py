# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


def func_power(num :int , pow: int) -> int:
    if pow==0:
        return 1
    if pow==1 :
        return num
    else:
        return num*func_power(num, pow-1)

def main():
    number=int(input("Введите число -> "))
    power=int(input("Введите степень - > "))

    print(func_power(number, power))

main()