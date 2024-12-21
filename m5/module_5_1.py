class House:
    def __init__(self, name, number_of_floors ):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует!")
        else:
            print(f'Всего этажей: {self.number_of_floors}')
            for i in range(1, new_floor+1):
                print(f'Этаж: {i}')



h1 = House('ЖК Ромашка', 10)
h1.go_to(5)