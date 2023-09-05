# Задача 3:Сложная задача: По желанию
# адача: НОП (наибольшая общая подпоследовательность) двух строк — это самая длинная последовательность 
# символов, которая содержится и в первой, и во второй строке, в том же порядке, но не обязательно подряд. 
# Другими словами, это максимально длинная последовательность символов, которая является "общей" для обеих строк.
# __
# Пример:

# makefile
# Copy code
# X = "AGGTAB"
# Y = "GXTXAYB"
# Наибольшая общая подпоследовательность: "GTAB" (другие НОП также могут быть "GTTAB" и "GTXAB").

# Задача состоит в том, чтобы написать программу, которая находит НОП для двух заданных строк.


def longest_common_subsequence(s1, s2):
    m = len(s1)
    n = len(s2)

    mas = [[0]*(n + 1) for _ in range(m + 1)]

    for i in range (1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j - 1]:
                mas[i][j] = mas[i - 1][j - 1] + 1
            else:
                mas[i][j] = max(mas[i - 1][j], mas[i][j - 1])


    result = ""
    i = m
    j = n 
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result = s1[i-1] + result
            i -= 1
            j -= 1
        elif mas[i - 1][j] > mas[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return result


x = "AGGTAB"
print(x)
y = "GXTXAYB"
print(y)

print(longest_common_subsequence(x, y))
