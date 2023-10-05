from slithering import Boa_Constrictor, Corn_Snake, Kingsnake, Python, Rat_Snake
from swimming import Catfish, Duck, Frog, Goldfish, Turtle
from walking import Donkey, Goat, Llama, Pig, Sheep


miss_fuzz = Llama("Miss Fuzz", "llama", "midday")

bramble = Donkey("Bramble", "donkey", "morning")

rosie = Goat("Rosie", "goat", "afternoon")

bailey = Sheep("Bailey", "sheep", "morning")

wilbur = Pig("Wilbur", "pig", "midday")

sunny = Corn_Snake("Sunny", "corn snake")

sly = Rat_Snake("Sly", "rat snake")

regal = Kingsnake("Regal", "kingsnake")

monty = Python("Monty", "python")

serpentine = Boa_Constrictor("Serpentine", "boa constrictor")

quackers = Duck("Quackers", "duck")

bubbles = Goldfish("Bubbles", "goldfish")

whiskers = Catfish("Whiskers", "catfish")

sheldon = Turtle("Sheldon", "turtle")

hopkins = Frog("Hopkins", "bullfrog")

print(f'{wilbur.name} the {wilbur.species} is available to pet during the {wilbur.shift} shift.')
