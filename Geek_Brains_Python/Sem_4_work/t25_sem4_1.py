# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()







# def main():
#     # input_str=input("Введите строку -> ")
#     # input_str=" ".join(input_str.split())

#     # input_str="a a a b c a a d c d d"
#     input_str="aaabcaadcdd"

#     print(input_str)

#     result_str=""
#     for i in range(1,len(input_str)):
#         count=0     
#         for j in range(0,len(input_str[:i])):
#             if input_str[j]==input_str[i-1]: count+=1
          
#         if count-1 !=0 : 
#             # result_str=result_str+input_str[i-1]+"_"+str(count-1)+" "
#             result_str=result_str+input_str[i-1]+"_"+str(count-1)
#         else: 
#             # result_str=result_str+input_str[i-1]+" "
#             result_str=result_str+input_str[i-1]

#     print(result_str)

# main()





# s = input('Введите строку: ')
# list_of_chars = list(s)
# letter_to_count = dict()
# for c in list_of_chars:   
#     if(c in letter_to_count):       
#         letter_to_count[c] = letter_to_count[c] + 1   
#     else:        
#         letter_to_count[c] = 0   
#     count_of_repeats = letter_to_count[c]   
#     print(f"{c}_{count_of_repeats}" if count_of_repeats > 0 else c, end=' ')






