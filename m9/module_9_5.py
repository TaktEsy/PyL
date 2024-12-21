class StepValueError(ValueError):
    """Пользовательское исключение для ошибки шага."""
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError("Шаг не может быть равен 0")
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start  # Инициализация указателя начальным значением

    def __iter__(self):
        self.pointer = self.start  # Сбрасываем указатель на начальное значение
        return self

    def __next__(self):
        # Условие завершения итерации в зависимости от знака шага
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration

        current = self.pointer  # Сохраняем текущее значение
        self.pointer += self.step  # Смещаем указатель на шаг
        return current

# Пример выполнения программы:
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print("Шаг указан неверно")

# Создание других объектов класса Iterator и их использование в цикле for
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

print()
for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()

