# Домашняя работа по уроку "Функции в Python.Функция с параметром"
# Задача "Матрица воплоти":

def get_matrix(n,m,value):
    # Сама матрица
    matrix = []
    print(f'Кол-во строк: {n}; Кол-во столбцов: {m}; Значения: {value}')
    if n != 0 and m != 0:
        for w in range(0, n):
            matrix.append(list())
            for r in range(0, m):
                matrix[w].append(value)
    else:
        print('Создание нулевой матрицы недопустимо')
        return False
    return matrix

print("Результат функции: ", get_matrix(2,2,10))
