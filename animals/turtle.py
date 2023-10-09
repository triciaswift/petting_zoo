from movements import Swimming, Walking
from .animal import Animal


class Turtle(Animal, Swimming, Walking):
    def __init__(self, name, species, food, chip_num, legs):
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self, legs)

    def feed(self):
        print(
            f'on {self.date_added.strftime("%m/%d/%Y")}, {self.name} had "Bye Bye Bye" hummed to it so it would eat its {self.food}'
        )
