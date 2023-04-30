#print("hello, world")
number = int(input("введите число -> ",))
print(number," -> ",end=" ")
sum=0
while number>0:
    sum=sum+number % 10
    number= number//10
print(sum)



