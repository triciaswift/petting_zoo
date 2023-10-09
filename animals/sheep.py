from movements import Walking
from .animal import Animal


class Sheep(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num, legs):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self, legs)
        self.shift = shift
