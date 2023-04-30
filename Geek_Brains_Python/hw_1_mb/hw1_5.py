n=int(input("введите N шоколадки -> ",))
m=int(input("введите M шоколадки -> ",))
k=int(input("введите количество кубиков K -> ",))
f1=False
i=min(n,m)
while ((not f1)and(i<n*m)):
    if ((k==i)or(k==n*m-i)): f1=True
    i=i+min(n,m)

f2=False
i=max(n,m)
while ((not f2)and(i<n*m)):
    if ((k==i)or(k==n*m-i)): f2=True
    i=i+max(n,m)

if f1 or f2: print("yes")
else: print("no")

