# Упражнение 6. Налоги и чаевые
# (Решено. 17 строк)
# Программа, которую вы напишете, должна начинаться с запроса у поль-
# зователя суммы заказа в ресторане. После этого должен быть произведен
# расчет налога и чаевых официанту. Вы можете использовать принятую
# в вашем регионе налоговую ставку для подсчета суммы сборов. В качестве
# чаевых мы оставим 18 % от стоимости заказа без учета налога. На выхо-
# де программа должна отобразить отдельно налог, сумму чаевых и итог,
# включая обе составляющие. Форматируйте вывод таким образом, чтобы
# все числа отображались с двумя знаками после запятой.

check_prise=int(input('Введите сумму счета в ресторане -> '))
print(f'чаевые = {check_prise*0.18}')
print(f'налог = {(check_prise-check_prise*0.18)*0.13}')
print(f'цена заказа = {check_prise-(check_prise-check_prise*0.18)*0.13-check_prise*0.18}')

print(f'общее = {check_prise*0.18 + (check_prise-check_prise*0.18)*0.13 + check_prise-(check_prise-check_prise*0.18)*0.13-check_prise*0.18} ')