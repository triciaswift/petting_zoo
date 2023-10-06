from movements import Swimming, Walking
from .animal import Animal


class Duck(Animal, Swimming, Walking):
    def __init__(self, name, species, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)

    def quack(self):
        print("The duck quacks. A lot.")

    def run(self):
        print(f"{self} waddles")
