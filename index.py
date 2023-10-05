from slithering import Boa_Constrictor, Corn_Snake, Kingsnake, Python, Rat_Snake
from swimming import Catfish, Duck, Frog, Goldfish, Turtle
from walking import Donkey, Goat, Llama, Pig, Sheep
from attractions import Petting_Zoo, Snake_Pit, Wetlands

# Create instances of animals
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

# Create instances of attractions
varmint_village = Petting_Zoo(
    "Varmint Village", "cute and fuzzy critters to cuddle")
slither_inn = Snake_Pit(
    "Slither Inn", "stupendous snakes of all sizes")
critter_cove = Wetlands(
    "Critter Cove", "full of feathered friends and fantastic fish")

# Add animals to attractions
varmint_village.animal_additions(miss_fuzz)
varmint_village.animal_additions(bramble)
varmint_village.animal_additions(rosie)
varmint_village.animal_additions(bailey)
varmint_village.animal_additions(wilbur)
slither_inn.animal_additions(sunny)
slither_inn.animal_additions(sly)
slither_inn.animal_additions(regal)
slither_inn.animal_additions(monty)
slither_inn.animal_additions(serpentine)
critter_cove.animal_additions(quackers)
critter_cove.animal_additions(bubbles)
critter_cove.animal_additions(whiskers)
critter_cove.animal_additions(sheldon)
critter_cove.animal_additions(hopkins)

# Output report to terminal
print(f"{varmint_village.attractions_name} is where you'll find {varmint_village.description}, like")
for animal in varmint_village.animals:
    print(f'    * {str(animal)}')

print(f"{slither_inn.attractions_name} is where you'll find {slither_inn.description}, like")
for snake in slither_inn.snakes:
    print(f'    * {str(snake)}')

print(f"{critter_cove.attractions_name} is where you'll find {critter_cove.description}, like")
for critter in critter_cove.aquatic_animals:
    print(f'    * {str(critter)}')


# sheldon.feed()  # If you do print(miss_fuzz.feed()) then None prints after message

# # bc of __str__ in the class we can do this and not get an error message
# print(monty)
