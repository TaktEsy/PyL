from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

# result = list(map(lambda x, y: (x, y), first, second))
result = list(map(lambda x, y: x == y, first, second))
print(result)
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:  # Открываем файл в режиме добавления
            for item in data_set:
                file.write(f"{str(item)}\n")  # Преобразуем каждый элемент в строку и записываем его в файл
    return write_everything


class MysticBall:
    def __init__(self, *words):
        self.words = words  # Сохраняем переданные строки в атрибут words

    def __call__(self):
        return choice(self.words)  # Возвращаем случайное слово из words


# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())  # Случайный выбор из ['Да', 'Нет', 'Наверное']
print(first_ball())  # Случайный выбор из ['Да', 'Нет', 'Наверное']
print(first_ball())  # Случайный выбор из ['Да', 'Нет', 'Наверное']

# Пример использования:
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

