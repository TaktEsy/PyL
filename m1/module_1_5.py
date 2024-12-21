immutable_var = ('Adam Kalinin', 2024, 23.9,)
print(immutable_var)
# Кортеж неизменяемый тип данных. Пример на строке ниже выдаст ошибку:
# immutable_var [0] = 'Vasya' -
# Кортежи поддерживают только конкатенацию и умножение
print("Поддержвиаемые операции с кортежами: ")
print(immutable_var[1] + immutable_var[2])
print(immutable_var[1] * immutable_var[2])

mutable_list = ['Anrey Ivanov', 'Ivan Andreev', 55, 3.14]
# Списки в свою очередь, изменяемый индексируемый тип данных
mutable_list[0] = "Jack Smoker"
mutable_list.append("Andrey Ivanov")
mutable_list.append(True)
mutable_list.extend("Name")
print(55 in mutable_list)
print(5 in mutable_list)

print(mutable_list)