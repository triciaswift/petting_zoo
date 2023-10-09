from movements import Swimming
from movements import Walking
from .animal import Animal


class Frog(Animal, Swimming, Walking):
    def __init__(self, name, species, food, chip_num, legs):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self, legs)

    def run(self):
        print(f"{self} jumps")
