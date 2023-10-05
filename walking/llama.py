from datetime import date


class Llama:

    def __init__(self, name, species, shift):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()  # YY-MM-DD
        self.walking = True
        self.shift = shift
