from slithering import Boa_Constrictor, Corn_Snake, Kingsnake, Python, Rat_Snake
from swimming import Catfish, Duck, Frog, Goldfish, Turtle
from walking import Donkey, Goat, Llama, Pig, Sheep


miss_fuzz = Llama("Miss Fuzz", "llama", "morning", "Llama Chow")

bramble = Donkey("Bramble", "donkey", "midday", "hay")

rosie = Goat("Rosie", "goat", "afternoon", "grains")

bailey = Sheep("Bailey", "sheep", "morning", "fruit")

wilbur = Pig("Wilbur", "pig", "midday", "vegetables")

sunny = Corn_Snake("Sunny", "corn snake", "mice")

sly = Rat_Snake("Sly", "rat snake", "mice")

regal = Kingsnake("Regal", "kingsnake", "lizards")

monty = Python("Monty", "python", "mice")

serpentine = Boa_Constrictor("Serpentine", "boa constrictor", "mice")

quackers = Duck("Quackers", "duck", "Waterfowl Pellets")

bubbles = Goldfish("Bubbles", "goldfish", "algae")

whiskers = Catfish("Whiskers", "catfish", "insects ")

sheldon = Turtle("Sheldon", "turtle", "fruit")

hopkins = Frog("Hopkins", "bullfrog", "insects")

sheldon.feed()  # If you do print(miss_fuzz.feed()) then None prints after message

# bc of __str__ in the class we can do this and not get an error message
print(monty)
