# Задача №37. Решение в группах
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def reccur_print(num :int):

    x= int(input("Введите число = "))
    if num==1 :
        print(x, end=" ")
        
    else:
        reccur_print(num-1)
        print(x, end=" ")
            

def main():
    count_number=int(input("Введите количество чисел -> "))
    
    reccur_print(count_number)

main()