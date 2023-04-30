# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

# def main():
#    n=int(input("введите число = ",)) 
#    result=1
#    for i in range(1,n+1):
#       result*=i
#    print(result)

# main()

def main():
   n=int(input("введите число = ",)) 
   result=1
   iter=1
   while iter<=n:
      result*=iter
      iter+=1
   print(result)

main()