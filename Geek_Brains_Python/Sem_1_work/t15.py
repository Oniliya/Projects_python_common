def main():
    n=int(input("введите общее количество арбузов = "),)
    min_a=n
    max_a=n
    for i in range(1,n+1):
        weight=int(input("введите массу арбуза = ",))
        if (weight>max_a): max_a=weight
        if (weight<min_a): min_a=weight
    print(min_a, max_a)

main()