#print("hello, world")
# number = int(input("введите число -> ",))
# print(number," -> (",end=" ")
# sum=0
# while number>0:
#     print(number % 10, end=" ")
#     sum=sum+number % 10
#     number= number//10
# print(") ", sum)



number = input("введите число -> ",)
part=number.split(".")
n1=int(part[0])
n2=int(part[1])
print(number," -> (",end=" ")
sum=0
while (n1>0)and(n2>0):
    print(n1 % 10, end=" ")
    sum=sum+n1 % 10
    n1= n1//10
    print(n2 % 10, end=" ")
    sum=sum+n2 % 10
    n2= n2//10

print(") ", sum)


