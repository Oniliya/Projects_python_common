
# Задача 2: Напишите программу, которая сортирует список чисел методом сортировки слиянием.

# Сортировка слиянием - это эффективный алгоритм сортировки, который разбивает список на две половины, сортирует их отдельно, 
# а затем объединяет в отсортированный список. Задача состоит в том, чтобы написать программу, 
# которая будет сортировать список чисел методом сортировки слиянием.

# Пример решения:

# Программа принимает на вход список чисел, который нужно отсортировать.
# Если список состоит из одного элемента или пуст, он считается уже отсортированным.
# В противном случае список разделяется на две половины.
# Рекурсивно вызывается сортировка слиянием для каждой половины.
# Затем отсортированные половины сливаются в один отсортированный список.
# Конечный отсортированный список возвращается.

import operator

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle], compare)
        right = merge_sort(L[middle:], compare)
        return merge(left, right, compare)
    

list1 = [78, 41, 4, 27, 3, 27, 8, 39, 19, 34, 6, 41, 13, 52, 16]
print(list1)
print(merge_sort(list1))