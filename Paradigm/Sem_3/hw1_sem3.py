# На Выбор Часть 1 или Часть 2

# Часть 1: Парадигмы программирования и ООП
# __
# Императивная vs Декларативная парадигма:
# Опишите задачу на Python, решение которой может быть представлено как императивное решение и как декларативное решение. 
# Объясните, в чем различие между двумя подходами и какой из них предпочтительнее в данном случае.
# __



# Императивный подход.
# Описываем последовательность шагов, которые надо выполнить.
# Разбиваем шаги на более мелкие до тех пор, пока каждый отдельный шаг не станет, по сути, одной командой. 
# В целом, продумываем и описываем то, как достичь нужного результата. 

# Декларативный подход.
# Описываем конечный результат и соотнисим его с исходными данными

# Возьмем для примера задачу: 
# Вычислить длинну гипотенузы треугольника

# Декларативный подход: 
# длина гипотенузы — это корень квадратный из суммы квадратов катетов

# Императивный подход:
# Берем первый катет, умножаем на себя, запоминаем, складываем и запоминаем результат. 
# Берем второй катет, умножаем на себя, запоминаем, добавляем к предыдущему результату и запоминаем. 
# Извлекаем корень из предыдущего результата.

result = 0
kat1 = int(input("введите длинну первого катета для прямоугольного треугольника = "))
kat2 = int(input("введите длинну второго катета для прямоугольного треугольника = "))
result += kat1*kat1
result += kat2*kat2
print (result ** 0.5)