class Slithering:
    def __init__(self, length):
        self.slither_speed = 0
        self.length = length

    def slither(self):
        print(f"{self} slithers")

    def animal_length(self):
        print(f"{self} is {self.length} feet long")
