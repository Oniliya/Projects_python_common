def main():
    n=int(input("введите общее количество монеток = ",))
    kol0=0
    kol1=0
    for i in range(1,n+1):
        mon=int(input())
        if (mon==0): kol0+=1
        else: kol1+=1
    if (kol1<=kol0):print(kol1)
    else:print(kol0)



main()