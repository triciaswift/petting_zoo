from animals import Animal


class Corn_Snake(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True
