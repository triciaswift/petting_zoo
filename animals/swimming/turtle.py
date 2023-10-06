from animals import Animal


class Turtle(Animal):

    def __init__(self, name, species, food, chip_num):
        super().__init__(name, species, food, chip_num)
        self.swimming = True

    def feed(self):
        print(
            f'on {self.date_added.strftime("%m/%d/%Y")}, {self.name} had "Bye Bye Bye" hummed to it so it would eat its {self.food}')
