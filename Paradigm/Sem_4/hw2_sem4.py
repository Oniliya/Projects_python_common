# Факториал: Напишите рекурсивную функцию для вычисления факториала числа n. 
# Факториал числа n обозначается как n! и равен произведению всех положительных целых чисел от 1 до n.
# __

def factorial(n: int) -> int:
    if (n==1) or (n==0): 
        return 1
    else: 
        return n*factorial(n-1)

print(factorial(10))