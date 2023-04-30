# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

def fibbon(num :int) -> int:
    if num==0:
        return 0
    if num==1:
        return 1
    else:
        return fibbon(num-1)+fibbon(num-2)

def main():
    number = int(input("Введите номер последовательности Фиббоначи - > "))
    for i in range(0, number+1):
        print(f"({i}, {fibbon(i)})", end=" ")



main()
