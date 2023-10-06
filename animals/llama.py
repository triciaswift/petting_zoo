from movements import Walking
from .animal import Animal


class Llama(Animal, Walking):
    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift

    def feed(self):
        print(
            f'on {self.date_added.strftime("%m/%d/%Y")}, {self.name} had "Rockytop" sung to it so it would eat its {self.food}'
        )
