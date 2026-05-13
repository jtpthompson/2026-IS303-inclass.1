'''

inputs:
- player level (int)
- player class (string)

processes:
- suggest a quest type based on player level and claass
- different quests for level ranges (1-10, 11-25, 26+)
- modified by class (mage, warrior, rouge)

outputs:
- print a recommended quest

'''

class_types = {
    "Mage" : ["Find a wand", "Find a spellbook", "Duel your professor"],
    "Warrior" : ["Find a sword", "Find a shield", "Defend your professor from the evil Mage."],
    "Rouge" : ["Find a cloak", "Find a knife", "Sneak your late homework into the professors inbox while he is fighting the Mage"]
    }

# Find a specific quest in the data structure
quest_to_find = input("What quest do you want? ")

for class_key in class_types:
    class_quests = class_types[class_key]
    for quest in class_quests:
        if quest == quest_to_find:
            print(f"Your quest if performed by the {class_key}")




player_class = input("What is your class? ").capitalize()
player_level = ""
while not player_level.isdigit():
    player_level = input("What is your current level? (Enter a whole number) ")

player_level = int(player_level)


# calculate quest leve based on the player level
quest_level = 0
if player_level >= 26:
    quest_level = 2
elif player_level >= 11:
    quest_level = 1

recommended_quest = class_types[player_class][quest_level]

print(f"You should od this quest: {recommended_quest}")

users_class_quests = class_types[player_class]
print(users_class_quests)
recommended_quest = users_class_quests[quest_level]
print(recommended_quest)