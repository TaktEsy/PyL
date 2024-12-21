class House:
    def __init__(self, name, number_of_floors):
        if not isinstance(number_of_floors, int):
            raise TypeError("Этажи должны быть целым числом!")
        self.name = name
        self.number_of_floors = number_of_floors


    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f"Название: {self.name}; Этажность: {self.number_of_floors}")

    def __eq__(self, other):
        return self.number_of_floors == other

    def __lt__(self, value):
        if not isinstance(value.number_of_floors, int):
            raise TypeError("Этажи должны быть целым числом!")
        return self.number_of_floors < value.number_of_floors

    def __le__(self, value):
        if not isinstance(value.number_of_floors, int):
            raise TypeError("Этажи должны быть целым числом!")
        return self.number_of_floors <= value.number_of_floors

    def __gt__(self, value):
        if not isinstance(value.number_of_floors, int):
            raise TypeError("Этажи должны быть целым числом!")
        return self.number_of_floors > value.number_of_floors

    def __ge__(self, value):
        if not isinstance(value.number_of_floors, int):
            raise TypeError("Этажи должны быть целым числом!")
        return self.number_of_floors >= value.number_of_floors

    def __ne__(self, value):
        if not isinstance(value.number_of_floors, int):
            raise TypeError("Этажи должны быть целым числом!")
        return self.number_of_floors != value.number_of_floors

    def __add__(self, value):
        if not isinstance(value, int):
            raise TypeError("Этажи должны быть целым числом!")
        return self.number_of_floors + value

    def __radd__(self, value):
        return self.__add__(self, value)

    def __iadd__(self, value):
        return self.__add__(self, value)

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует!")
        else:
            print(f'Всего этажей: {self.number_of_floors}')
            for i in range(1, new_floor+1):
                print(f'Этаж: {i}')


h1 = House('Бурдж-Халифа', 163)
h2 = House('Куала-Лумпур', 118)

print(h1)
print(h2)
print(h2.number_of_floors)

# __eq__

print("__eq__")
print(h1 == h2)
print("_________")

# __add__
print("__add__")
h2.number_of_floors = h2+45
print(h1)
print(h2)
print(h1 == h2)
print("_________")

print("__iadd__")
h2.number_of_floors += 0
print(h2)
print("_________")

print("__radd__")
h2.number_of_floors = 1 + h2.number_of_floors
print(h2)
print("_________")

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
