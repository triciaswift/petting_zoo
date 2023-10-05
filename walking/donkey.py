from datetime import date


class Donkey:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
        self.shift = shift
        self.food = food

    def feed(self):
        print(
            f'{self.name} was fed {self.food} on {self.date_added.strftime("%m/%d/%Y")}')
