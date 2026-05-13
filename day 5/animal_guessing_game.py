'''

Inputs:
- A string containing an attribute guess or the guess of the animal's name.

Processes:
- Validate their entry to make sure that it is a string.
- Randomly select an animal.
- Allow the user to guess until they guess the correct animal.
- when they gyess, tell them if the animal has the attribute or not.
- Tell the user when they guess correctly.


Outputs:
- Attribute guess correctness
- Congratulations message


'''


import random     #This teaches Python how to do random stuff

ANIMALS = {
    "Lion" : ["Mammal", "Four legs", "Predator", "Savannah", "Cat", "Land", "Yellow", "Africa", "Fur"],
    "Hyena" : ["Mammal", "Four legs", "Predator", "Spots", "Scavenger", "Land", "Claws", "Yellow", "Fur"],
    "Shark" : ["Fish", "Fins", "Predator", "Sea", "Skin"],
    "Pigeon" : ["Bird", "Wings", "Two legs", "Feathers", "City", "Scavenger", "Omnivore", "Flies", "Gray"],
    "Bunny" : ["Mammal", "Four legs", "Soft", "Fur", "Small", "Pet", "Cute", "Prey"],
    "Snake" : ["Reptile", "Scales", "No legs", "Land", "Pet", "Pedator"],
    "Panther" : ["Mammal", "Claws", "Black", "Spots", "Predator", "Jungle", "Carnivore", "Four legs", "Climbs trees", "Cat", "Fur"],
    "Eagle" : ["Bird", "Two legs", "Wings", "Predator", "Carnivore", "Flies", "Talons", "Solitary", "Feathers"],
    "Chicken" : ["Bird", "Two legs", "Wings", "Scavenger", "Omnivore", "Flocks", "Feathers"],
    "Human" : ["Mammal", "Fingers", "Omnivores", "Two legs", "Fur"],
    "Turtle" : ["Amphibean", "Four legs", "Omnivore", "Green", "Swim", "Shell", "Bite"]

}

WELCOME_MESSAGE = """Animal guessing game
I have pickeda random animal. Guess an
attribute or the name of the animal.
"""

CONGRATULATIONS_MESSAGE = "You won!"


list_of_animal_names = list(ANIMALS.keys())
random_animal = random.choice(list_of_animal_names)
random_animal_attributes = ANIMALS[random_animal]


guess = ""

while guess != random_animal:
    guess = input("Please guess an attrubute or an animal: ").capitalize()
    if guess in random_animal_attributes:
        print(f"Yes, {guess} is an attribute of the animal.")
    elif guess == random_animal:
        print(CONGRATULATIONS_MESSAGE)
    else:
        print(f"No, {guess} is not an attribute of the animal.")
