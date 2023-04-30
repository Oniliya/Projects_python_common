# Упражнение 13. Размен
# (Решено. 35 строк)
# Представьте, что вы пишете программное обеспечение для автомати-
# ческой кассы в магазине самообслуживания. Одной из функций, зало-
# женных в кассу, должен быть расчет сдачи в случае оплаты покупателем
# наличными.
# Напишите программу, которая будет запрашивать у пользователя сум-
# му сдачи в центах. После этого она должна рассчитать и вывести на экран,
# сколько и каких монет потребуется для выдачи указанной суммы, при ус-
# ловии что должно быть задействовано минимально возможное количество
# монет. 
# Допустим, у нас есть в распоряжении монеты достоинством в 1,
# 5, 10, 25 центов, а также в 1 (loonie) и 2 (toonie) канадских доллара.

# Примечание. Монета номиналом в 1 доллар была выпущена в Канаде в 1987 году.
# Свое просторечное название (loonie) она получила от изображения полярной гагары
# (loon) на ней. Двухдолларовая монета, вышедшая девятью годами позже, была про-
# звана toonie, как комбинация из слов два (two) и loonie.

my_sum=int(input('Введите сумуму сдачи в центах -> '))

cent1, cent5, cent10, cent25, loonie, toonie = 1, 5, 10, 25, 100, 200

print(f'{my_sum//toonie}, toonie' if my_sum//toonie !=0 else ''  )
my_sum=my_sum%toonie

print(f'{my_sum//loonie}, loonie' if my_sum//loonie !=0 else ''  )
my_sum=my_sum%loonie

print(f'{my_sum//cent25}, cent25' if my_sum//cent25 !=0 else ''  )
my_sum=my_sum%cent25

print(f'{my_sum//cent10}, cent10' if my_sum//cent10 !=0 else ''  )
my_sum=my_sum%cent10

print(f'{my_sum//cent5}, cent5' if my_sum//cent5 !=0 else ''  )
my_sum=my_sum%cent5

print(f'{my_sum//cent1}, cent1' if my_sum//cent1 !=0 else ''  )
my_sum=my_sum%cent1

