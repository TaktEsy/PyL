class House:
    def __init__(self, name, number_of_floors ):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return (f"Название {self.name}; Этажность: {self.number_of_floors}")
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует!")
        else:
            print(f'Всего этажей: {self.number_of_floors}')
            for i in range(1, new_floor+1):
                print(f'Этаж: {i}')



h1 = House('ЖК Эльбрус', 10)
print(h1)
print(len(h1))

h2 = House('Бурдж-Халифа', 163)
print(h2)
print(len(h2))
