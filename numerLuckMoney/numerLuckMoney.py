﻿ #импортируем математическую библиотеку:
import math

#просим ввести переменные:
den=int(input("Введите день рождения:"))

mesyac=int(input("Введите месяц рождения:"))

god=int(input("Введите год рождения:"))

 #делаем списки из чисел дат:
список_из_дня = [(den//(10**i))%10 for i in range(math.ceil(math.log(den, 10))-1, -1, -1)]
список_из_месяца = [(mesyac//(10**i))%10 for i in range(math.ceil(math.log(mesyac, 10))-1, -1, -1)]
список_из_года = [(god//(10**i))%10 for i in range(math.ceil(math.log(god, 10))-1, -1, -1)]

#заменяем девятки на нули с помощью математическ.библиотеки:
for i, n in enumerate(список_из_дня):
  if n == 9:
     список_из_дня[i] = 0

for i, n in enumerate(список_из_месяца):
  if n == 9:
     список_из_месяца[i] = 0

for i, n in enumerate(список_из_года):
  if n == 9:
     список_из_года[i] = 0

     """
#выводим списки:
print(список_из_дня)
print(список_из_месяца)
print(список_из_года)
"""

#складываем числа из списков
сумма_чисел_из_дня = sum(список_из_дня)
сумма_чисел_из_месяца = sum(список_из_месяца)
сумма_чисел_из_года = sum(список_из_года)

"""
#выводим суммы чисел:
print(сумма_чисел_из_дня)
print(сумма_чисел_из_месяца)
print(сумма_чисел_из_года)
"""
#делаем список_из_суммы_чисел_из_года, т.к. там двузначные числа-и получаем сумму_из_списка_из_суммы_чисел_из_года:
список_из_суммы_чисел_из_года = [(сумма_чисел_из_года//(10**i))%10 for i in range(math.ceil(math.log(сумма_чисел_из_года, 10))-1, -1, -1)]
сумма_из_списка_из_суммы_чисел_из_года = sum(список_из_суммы_чисел_из_года)

"""
#выводим суммы чисел:
print(сумма_чисел_из_дня)
print(сумма_чисел_из_месяца)
print(сумма_из_списка_из_суммы_чисел_из_года)
"""
#складываем все суммы чисел:
сумма_всех_сумм_чисел = сумма_чисел_из_дня + сумма_чисел_из_месяца + сумма_из_списка_из_суммы_чисел_из_года
#делаем список из сумма_всех_сумм_чисел для того чтоб потом его сложить:
список_из_суммы_всех_сумм_чисел = [(сумма_всех_сумм_чисел//(10**i))%10 for i in range(math.ceil(math.log(сумма_всех_сумм_чисел, 10))-1, -1, -1)]
полная_сумма_всех_сумм_чисел = sum(список_из_суммы_всех_сумм_чисел)



#создаем строку из сумм чисел:
print("ВАШ ДЕНЕЖНЫЙ КОД: "f"{сумма_чисел_из_дня}{сумма_чисел_из_месяца}{сумма_из_списка_из_суммы_чисел_из_года}{полная_сумма_всех_сумм_чисел}")