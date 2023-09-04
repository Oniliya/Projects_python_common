# Фибоначчи через рекурсию: Напишите рекурсивную функцию для вычисления числа Фибоначчи с индексом n. 
# Напоминаю, что последовательность Фибоначчи определяется как: F(0) = 0, F(1) = 1 и F(n) = F(n-1) + F(n-2) для n > 1.
# __


def fibbonachi(n: int) -> int:
    if (n==0):
        return 0
    elif (n==1):  
        return 1
    else: 
        return fibbonachi(n-1)+fibbonachi(n-2)

print(fibbonachi(5))


