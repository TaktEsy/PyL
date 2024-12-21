my_dict = {'Adam': 2000, 'Petr': 1337, 'Masha': 2004, 'Arnold': 1999}
print(my_dict)

print(my_dict['Petr'])  # Вывод значения по существующему ключу
print(my_dict.get('Egor'))  # Вывод значения по несуществующему ключу без ошибки

# Плюс 2 произвольные пары в словарь
my_dict['Sofia'] = 2006
my_dict['Napoleon'] = 1769

# Удаление одной из пар по ключу и вывод значения этой удаленной пары
dlt = my_dict.pop('Adam')
print(dlt)

# Вывод словаря
print(my_dict)

# Множества
my_set = {1, True, 99, 'Истина'}
print(my_set)
my_set.add('Новая строка')
my_set.add('Ещё одна строка')
my_set.discard(1)
print(my_set)