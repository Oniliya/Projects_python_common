# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 

# Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам 
# Парам пам-пам

ALPHABET='уеыаоэяиюё'

def count_alp(my_list :list):
    list_2=set()
    for i in my_list:
        sum_sl=0
        for k in i:
            sum_sl=sum_sl+1 if k in ALPHABET else sum_sl
        list_2.add(sum_sl)

    return True if len(list_2)==1 else False

puh_list=list(input("введите стихотворение Винни-Пуха -> ").lower().split())    

print('{}'.format('Парам пам-пам' if count_alp(puh_list) else 'Пам парам'))
