from datetime import date


class Duck:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        print(
            f'{self.name} was fed {self.food} on {self.date_added.strftime("%m/%d/%Y")}')
