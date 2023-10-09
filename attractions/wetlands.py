from .attraction import Attraction


class Wetlands(Attraction):
    def __init__(self, name, description):
        super().__init__(name, description)

    # Duck typing check
    def add_animal_pythonic(self, animal):
        try:
            if animal.swim_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(
                f"{animal} doesn't know how to swim, so please do not put it in the {self.attraction_name} attraction."
            )
