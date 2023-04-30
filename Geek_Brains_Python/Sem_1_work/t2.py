
k1=int(input('колмчество учащихся в первом классе = '))
k2=int(input('количество учащихся во втором классе = '))
k3=int(input('количество учащихся в третьем классе = '))
# kol_desk=0
# if (k1%2==0): kol_desk+=k1//2
# else: kol_desk+=k1//2+1
# if (k2%2==0): kol_desk+=k2//2
# else: kol_desk+=k2//2+1
# if (k3%2==0): kol_desk+=k3//2
# else: kol_desk+=k3//2+1
# print(kol_desk)

print(k1//2+k1%2 + k2//2+k2%2 + k3//2+k3%2)
