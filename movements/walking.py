class Walking:
    def __init__(self, legs):
        self.walk_speed = 0
        self.legs = legs

    def run(self):
        print(f"{self} walks")

    def leg_num(self):
        print(f"{self} has {self.legs} legs")
