from pprint import pprint
class Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return str(f"{self.name, self.weight, self.category}")


class Shop():
    __file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            products = file.read()
        return products

    def add(self, *products):
        with open(self.__file_name, 'a+') as file:
            for product in products:
                file.seek(0)
                if any(product.name in line for line in file):
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    file.write(f'{product.name}, {product.weight}, {product.category}\n')
        # file = open(self.__file_name, 'r')
        # pprint(products)
        #file.write(products)


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p1) # __str__
print(p2) # __str__
print(p3) # __str__

print("add")
s1.add(p1, p2, p3)

print("get")
print(s1.get_products())
print()