number=input("введите номер билета -> ",)
part1=number[:3]
part2=number[3:6]
if ((int(part1[0])+int(part1[1])+int(part1[2]))==((int(part2[0])+int(part2[1])+int(part2[2])))) :
    print("yes")
else:
    print("no")

