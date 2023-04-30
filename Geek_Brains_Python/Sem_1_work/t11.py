def main():
    n=int(input("введите число = ",))
    f=False
    if (n==1):print("1 или 2 элемент")
    elem1=1
    elem2=1
    for iter in range(3,n+10):
        elem1_1=elem2
        elem2=elem1+elem2
        elem1=elem1_1        
        if (n==elem1) or (n==elem2) :
            print(iter)
            f=True
            break
    if not f : print("-1")
        

main()