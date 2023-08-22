# **Процедурное программирование:

# Разбиение массива на подмассивы:**
# __
# Задание: Напишите функцию, которая принимает массив чисел и значение X. 
# Функция должна возвращать массив подмассивов так, чтобы сумма чисел в каждом подмассиве была меньше или равна X.
# Входные данные:
# Массив чисел длиной N.
# Число X.
# Выходные данные:
# Массив подмассивов.
# __

def find_sub_arr(my_list: list, num: int) -> list:
    result = list([])
    for i in range(0, len(my_list)):
        sum_list = 0
        for j in range(i, len(my_list)):
            sum_list = sum_list + my_list[j]
            
            if (sum(my_list[i:j+1])<=num):
                result.append(my_list[i:j+1])
    return result

if __name__ == "__main__":

    my_list = [0, 5, 43, 25, 2, -2, 6, 8, 9, 10, 11, 3]
    x = int(input("введите число = "))
    
    print(find_sub_arr(my_list, x))