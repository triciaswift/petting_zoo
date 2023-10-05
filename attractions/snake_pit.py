class Snake_Pit:

    def __init__(self, name, description):
        self.attractions_name = name
        self.description = description
        self.snakes = list()

    def animal_additions(self, snake):
        self.snakes.append(snake)
