# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# 1 1 2 3 5 8 13 21 34


n=int(input("введите число = ",))
elem1=1
elem2=1
iter=3
while (elem2<n):
    elem1, elem2 = elem2, elem1+elem2
    iter+=1

print(iter if elem2==n else -1)



# n=int(input("введите число = ",))
# if (n==1):print("1 или 2 элемент")
# elem1=1
# elem2=1
# iter=3
# while (elem1<n)and(elem2<n):
#     elem1_1=elem2
#     elem2+=elem1
#     elem1=elem1_1        
#     iter+=1
#     if (n==elem1) or (n==elem2): print(iter)




# def main():
#     n=int(input("введите число = ",))
#     f=False
#     if (n==1):print("1 или 2 элемент")
#     elem1=0
#     elem2=1
#     for iter in range(3,n+10):
#         elem1_1=elem2
#         elem2=elem1+elem2
#         elem1=elem1_1        
#         if (n==elem1) or (n==elem2) :
#             print(iter)
#             f=True
#             break
#     if not f : print("-1")

# main()
