

def personal_sum(numbers):
    res = 0
    incorrect_data = 0

    for n in numbers:
        try:
            res += n
        except TypeError as ext:
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы: {n}")

        # try:
        #     res = 0
        #     res = res+n
        # except TypeError:
        #
        #     incorrect_data += 1
        # return res, incorrect_data
    return res, incorrect_data

def calculate_average(numbers):
    try:
        ave = personal_sum(numbers)[0] / (len(numbers) - personal_sum(numbers)[1])
        return ave
    except TypeError:
        print("В numbers записан некорректный тип данных")
    except ZeroDivisionError:
        return 0
        print("На ноль не делим!")



print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 58,])}') # Всё должно работать
print()