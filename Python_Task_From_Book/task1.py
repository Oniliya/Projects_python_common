# Упражнение 1. Почтовый адрес
# (Решено. 9 строк)
# Напишите несколько строк кода, выводящих на экран ваше имя и почто-
# вый адрес. Адрес напишите в формате, принятом в вашей стране. Ника-
# кого ввода от пользователя ваша первая программа принимать не будет,
# только вывод на экран и больше ничего.

# print("153025")
# print("Россия")
# print("-")
# print("-")

# import os module  
from os import system, name  
 
# sleep module to display output for some time period  
from time import sleep  
 
# define the clear function  
def clear():  
 
 # for windows  
#  if name == 'nt':  
    _ = system('cls')  
 
#  # for mac and linux(here, os.name is 'posix')  
#  else:  
#     _ = system('clear')  
 
# print out some text  
print('Hello\n'*10)  
 
# sleep time 2 seconds after printing output  
sleep(5)  
 
# now call function we defined above  
clear()  

print("153025")
print("Россия")
print("-")
print("-")