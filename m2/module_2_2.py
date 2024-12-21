# 2023/09/28 00:00|Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."

first = input('Первое число: ')
second = input('Второе число: ')
third = input('Третье число: ')

if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif first != second != third:
    print(0)
