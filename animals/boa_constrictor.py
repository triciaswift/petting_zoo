from movements import Slithering
from .animal import Animal


class Boa_Constrictor(Animal, Slithering):
    def __init__(self, name, species, food, chip_num, length):
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self, length)

    def feed(self):
        print(
            f"on {self.date_added.strftime('%m/%d/%Y')}, {self.name} had it's belly rubbed so it would eat its {self.food}"
        )
