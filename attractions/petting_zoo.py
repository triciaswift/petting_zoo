class Petting_Zoo:

    def __init__(self, name, description):
        self.attractions_name = name
        self.description = description
        self.animals = list()

    def animal_additions(self, animal):
        self.animals.append(animal)