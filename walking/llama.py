from datetime import date


class Llama:

    def __init__(self, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()  # YY-MM-DD
        self.walking = True
        self.shift = shift
        self.food = food

    def __str__(self):
        return f"{self.name} the {self.species}"

    def feed(self):
        print(
            f'{self.name} was fed {self.food} on {self.date_added.strftime("%m/%d/%Y")}')
