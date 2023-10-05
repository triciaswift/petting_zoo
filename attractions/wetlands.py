class Wetlands:

    def __init__(self, name, description):
        self.attractions_name = name
        self.description = description
        self.aquatic_animals = list()

    def animal_additions(self, animal):
        self.aquatic_animals.append(animal)
