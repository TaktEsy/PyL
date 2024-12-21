import threading
import time

class Knight(threading.Thread):

    def __init__(self, name, power, enemy=100):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)
        self.enemy = enemy
        self.period = 0


    def run(self):
        print(f"{self.name}, на нас напали!")

        while self.enemy:
            period =+ 1

            # Убийство врага
            self.enemy -= self.power

            # Счетчик дней
            self.period += 1


            print(f"{self.name}, сражается {self.period} дней(дня), осталось {self.enemy} врагов!")

            # Сообщение о победе
            if self.enemy == 0:
                print(f"{self.name}, одержал победу спустя {self.period} дней(дня)!")


k1 = Knight('Versetto', 10)
k2 = Knight('Galahad ', 20)
k1.start()
k2.start()
