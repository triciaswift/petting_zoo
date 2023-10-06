from datetime import date


class Animal:
    def __init__(self, name, species, food, chip_num):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.food = food
        self.__chip_number = chip_num
        self.date_added = date.today()  # YY-MM-DD

    def __str__(self):
        return f"{self.name} the {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    @property  # The getter
    def chip_number(self):
        return self.__chip_number  # returns a private value

    @chip_number.setter  # The setter
    def chip_number(self, num):
        pass    # prevents the user from setting the value for chip_number
