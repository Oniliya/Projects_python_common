# __
# Ленивые вычисления: Напишите функцию, которая будет генерировать бесконечную последовательность простых чисел. 
# Используйте ленивые вычисления, чтобы генерировать только те числа, которые действительно нужны.


def prime_generator(last_num):
    prime_lst = {}
    p = 1
    while p < last_num:
        if p not in prime_lst:
            yield p
            prime_lst[p * p] = [p]
        else:
            for s in prime_lst[p]:
                prime_lst.setdefault(s + p, []).append(s)
            del prime_lst[p]
 
        p += 1
 
 
print(*prime_generator(5000))