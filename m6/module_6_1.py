class Animal():
    alive = True
    fed = False # Накормленный
    name = "Default"

    def __init__(self, name):
        self.name = name


    def eat(self, food):
        if self.fed == False:
            if food.edible == True:
                self.fed = True
                self.alive = True
                print (f'{self.name} съел {food.name}')
            else:
                self.alive = False
                self.fed = True
                print(f'{self.name} не стал есть {food.name}')



class Plant():
    edible = False
    name = "Default"

    def __init__(self, name):
        self.name = name
        if name == 'Цветик семицветик':
            self.edible = False
        elif name == 'Заводной апельсин':
            self.edible = True



class Mammal(Animal):
    pass

class Predator(Animal):
    pass
class Flower(Plant):
    edible = False

class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print('==============================')

a1.eat(p1)
# print(p1.edible)
print(f'Живой:{a1.alive}')
print(f'Накормленный: {a1.fed}')


print('==============================')

a2.eat(p2)
# print(p2.edible)
print(f'Живой: {a2.alive}')
print(f'Накормленный: {a2.fed}')
