n=int(input("введите количество дней = ",))
max_=0
max_new=0
for i in range(1,n+1):
    date_tem=int(input())
    if (date_tem>0):
        max_new += 1
        if (max_new>max_):max_=max_new
    else: max_new=0
print(max_)