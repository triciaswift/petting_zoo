from datetime import date


class Catfish:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(
            f'{self.name} was fed {self.food} on {self.date_added.strftime("%m/%d/%Y")}')
