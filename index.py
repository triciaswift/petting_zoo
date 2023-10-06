from animals import (
    Boa_Constrictor,
    Corn_Snake,
    Kingsnake,
    Python,
    Rat_Snake,
    Catfish,
    Duck,
    Frog,
    Goldfish,
    Turtle,
    Donkey,
    Goat,
    Llama,
    Pig,
    Sheep,
)
from attractions import Petting_Zoo, Snake_Pit, Wetlands

# Create instances of animals
miss_fuzz = Llama("Miss Fuzz", "llama", "morning", "Llama Chow", 123456)
bramble = Donkey("Bramble", "donkey", "midday", "hay", 123789)
rosie = Goat("Rosie", "goat", "afternoon", "grains", 987654)
bailey = Sheep("Bailey", "sheep", "morning", "fruit", 456789)
wilbur = Pig("Wilbur", "pig", "midday", "vegetables", 654321)
sunny = Corn_Snake("Sunny", "corn snake", "mice", 234567)
sly = Rat_Snake("Sly", "rat snake", "mice", 765432)
regal = Kingsnake("Regal", "kingsnake", "lizards", 345678)
monty = Python("Monty", "python", "mice", 876543)
serpentine = Boa_Constrictor("Serpentine", "boa constrictor", "mice", 567890)
quackers = Duck("Quackers", "duck", "Waterfowl Pellets", 321098)
bubbles = Goldfish("Bubbles", "goldfish", "algae", 678901)
whiskers = Catfish("Whiskers", "catfish", "insects", 890123)
sheldon = Turtle("Sheldon", "turtle", "fruit", 432109)
hopkins = Frog("Hopkins", "bullfrog", "insects", 109876)

# Create instances of attractions
varmint_village = Petting_Zoo("Varmint Village", "cute and fuzzy critters to cuddle")
slither_inn = Snake_Pit("Slither Inn", "stupendous snakes of all sizes")
critter_cove = Wetlands("Critter Cove", "full of feathered friends and fantastic fish")

# Add animals to attractions
varmint_village.add_animal(miss_fuzz)
varmint_village.add_animal(bramble)
varmint_village.add_animal(rosie)
varmint_village.add_animal(bailey)
varmint_village.add_animal(wilbur)
slither_inn.add_animal(sunny)
slither_inn.add_animal(sly)
slither_inn.add_animal(regal)
slither_inn.add_animal(monty)
slither_inn.add_animal(serpentine)
critter_cove.add_animal(quackers)
critter_cove.add_animal(bubbles)
critter_cove.add_animal(whiskers)
critter_cove.add_animal(sheldon)
critter_cove.add_animal(hopkins)


# * ------------------Food Function Fun------------------
# sheldon.feed()  # If you do print(miss_fuzz.feed()) then None prints after message

# # bc of __str__ in the class we can do this and not get an error message
# print(monty)

# * -------------Composing Coming Attractions-------------
# # Output report to terminal
# print(
#     f"{varmint_village.attraction_name} is where you'll find {varmint_village.description}, like"
# )
# for animal in varmint_village.animals:
#     print(f"    * {animal}")

# print(
#     f"{slither_inn.attraction_name} is where you'll find {slither_inn.description}, like"
# )
# for animal in slither_inn.animals:
#     print(f"    * {animal}")

# print(
#     f"{critter_cove.attraction_name} is where you'll find {critter_cove.description}, like"
# )
# for animal in critter_cove.animals:
#     print(f"    * {animal}")

# * ---------------Controlling the Animals----------------
# bramble.chip_number = 555783  # the setter function prevents this

# print(bramble.chip_number)  # prints what was originally assigned

# print(slither_inn.last_critter_added)
# print(varmint_village.last_critter_added)
# print(critter_cove.last_critter_added)

# * --------------Eliminating Class Waste-----------------
# miss_fuzz.feed()
# sheldon.feed()
# serpentine.feed()
# quackers.feed()

# *---------------Complex, Clean Critter Classes-----------
# serpentine.slither()
# quackers.run()
# quackers.swim()
# wilbur.oink()

# *----------------If it Honks Like a Goose-----------------
