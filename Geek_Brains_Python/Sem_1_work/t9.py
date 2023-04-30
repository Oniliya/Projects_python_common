# def main():
#    n=int(input("введите число = ",)) 
#    result=1
#    for i in range(1,n+1):
#       result*=i
#    print(result)

# main()

def main():
   n=int(input("введите число = ",)) 
   result=1
   iter=1
   while iter<=n:
      result*=iter
      iter+=1
   print(result)

main()