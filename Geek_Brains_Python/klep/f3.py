s=input("введите строку  ",)
list_my =list()
max_=0
for i in range(len(s)//2):
    t=s[:i+1]
    sq=list()
    for j in range(0,len(s),len(t)): sq.append(s[j:j+len(t)])
    f=True
    j=0
    while (f and j<len(sq)-1):
        if sq[j] != sq[j+1]: f=False
        j=j+1
    if (f):
        if len(sq)>max_ : max_=len(sq)
print(max_)
