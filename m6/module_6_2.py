class Vehicle():
    owner: str
    __model: str
    __engine_power: int
    __color: str
    __COLOR_VARIANTS = 'blue', 'yellow', 'red', 'green', 'black', 'white'

    def __init__(self, owner, model, color, eng_power):
        self.owner = str(owner)
        self.__model = str(model)
        self.__engine_power = int(eng_power)
        self.__color = str(color)

    def get_model(self):
        print(f"Модель: {self.__model}")

    def get_horsepower(self):
        print(f"Мощность двигателя: {self.__engine_power}")

    def get_color(self):
        print(f"Цвет: {self.__color}")

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color.lower()
        else:
            print(f'Недопустимый цвет: {new_color}')
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('FEBos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('Black')
vehicle1.owner = 'Vasyok'
print('============================')
vehicle1.print_info()
