def main():
    s=int(input())
    p=int(input())
    for i in range(max(s,p)):
        for j in range(max(s,p)):
            if (i+j==s)and(i*j==p):
                print(i,j)
                break
    


main()