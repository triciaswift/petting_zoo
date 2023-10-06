from animals import Animal


class Boa_Constrictor(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.slithering = True

    def feed(self):
        print(
            f"on {self.date_added.strftime('%m/%d/%Y')}, {self.name} had it's belly rubbed so it would eat its {self.food}")
