from datetime import date


class Llama:

    def __init__(self, name, species, shift, food, chip_num):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()  # YY-MM-DD
        self.walking = True
        self.shift = shift
        self.food = food
        self.__chip_number = chip_num

    def __str__(self):
        return f"{self.name} the {self.species}"

    def feed(self):
        print(
            f'{self.name} was fed {self.food} on {self.date_added.strftime("%m/%d/%Y")}')

    @property  # The getter
    def chip_number(self):
        return self.__chip_number  # returns a private value

    @chip_number.setter  # The setter
    def chip_number(self, number):
        pass  # prevents the user from setting the value for chip_number
