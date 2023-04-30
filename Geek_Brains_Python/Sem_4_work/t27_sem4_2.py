# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13


import string 

def main():
    input_str="She sells sea shells on the sea shore The shells that "\
        "she sells are sea shells I'm sure.So if she sells sea shells "\
            "on the sea shore I'm sure that the shells are sea shore shells"
    # input_str=input("Введите строку -> ").lower()
    
    # input_str=" ".join(input_str.split())

    for ch in string.punctuation:
        input_str = input_str.replace(ch,"")

    print(input_str)

    count_mn=set(input_str.split())

    print(count_mn)
    
    print(len(count_mn))
main()



# str_split = input("Enter some text: ").lower().split()
# str_cnt = {}
# for i in str_split:
#     str_cnt[i] = str_cnt.get(i, 0) + 1
# print(f"Number of words in the text is: {len(str_cnt)}")