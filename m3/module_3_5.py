
def gmd(number):
    str_number = str(number)

    # Получаем первый символ строки и переводим в целочисленный
    first = int(str_number[0])

    print(first, type(first))

    # Начало рекурсии
    if str_number.__len__() <= 1:
        return first
    else:
        # Выход из рекурсии
        return first * gmd(int(str_number[1:]))

print(gmd(40203))