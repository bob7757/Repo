
# Problems: Currently damage values are rolled once in the beginning and saved. I think i can change this but idk how.
# Also: The only stats i used so far are hp, dodge chance, defense, and magic defense. I need to learn how to use
# functions really bad.
# Random imported for hit calculations as well as some damage calcs
import random
# Custom class to store all the stats of my classes, probably could have used an ordered list but this seemed like a good
# chance to test it out
class Character:
    def __init__(self, hit_points, mana_points, strength, intelligence, dodge_chance, defense, magic_defense, attacks, damage, hit_chance, attack_quantity):
        self.hit_points = hit_points
        self.mana_points = mana_points
        self.strength = strength
        self.intelligence = intelligence
        self.dodge_chance = dodge_chance
        self.defense = defense
        self.magic_defense = magic_defense
        self.attacks = attacks
        self.damage = damage
        self.hit_chance = hit_chance
        self.attack_quantity = attack_quantity



# Defining the different parts of each class
fighter_attack_names = ["Stab", "Slash", "Flurry"]
fighter_Damage = {"Stab": 13, "Slash": 10, "Flurry": 7}
fighter_hit_chance = {"Stab": 100, "Slash": 90, "Flurry": 50}
fighter_attack_times = {"Stab": 1, "Slash": 1, "Flurry": 3}
mage_attack_names = ["Firebolt", "Ray of Frost", "Magic Missile", "Explosion"]
mage_damage = {"Firebolt": 8, "Ray of Frost": 10, "Magic Missile": 7, "Explosion": 55}
mage_hit_chance = {"Firebolt": 100, "Ray of Frost": 90, "Magic Missile": 50, "Explosion": 20}
mage_attack_times = {"Firebolt": 1, "Ray of Frost": 1, "Magic Missile": 3, "Explosion": 1}


fighter = Character(100, 0, 10, 0, 10, 10, 0, fighter_attack_names, fighter_Damage, fighter_hit_chance, fighter_attack_times)
mage = Character(80, 100, 0, 10, 10, 0, 10, mage_attack_names, mage_damage, mage_hit_chance, mage_attack_times)

player_1 = "player_1"
player_2 = "player_2"

# Players selecting their character, tried a function but i couldnt get it to return the right thing so i gave up.
while player_1 == "player_1":
    player_select = input("Player 1 would you like to play as the fighter of the mage?").lower()
    if player_select == "fighter":
        print("You have selected fighter.")
        player_1 = fighter
    elif player_select == "mage":
        print("You have selected mage.")
        player_1 = mage
    else:
        print("Please choose fighter or mage")


while player_2 == "player_2":
    player_select = input("Player 2 would you like to play as the fighter of the mage?").lower()
    if player_select == "fighter":
        print("You have selected fighter.")
        player_2 = fighter
    elif player_select == "mage":
        print("You have selected mage.")
        player_2 = mage
    else:
        print("Please choose fighter or mage.")

# Turn order randomizer, later add contested speed stat?
player_1_turn = False
hit =  []
order = random.randint(1,2)
if order == 1:
    player_1_turn = True
    print("Player 1 goes first!")
else:
    player_1_turn = False
    print("Player 2 goes first!")

# Battle time
while player_1.hit_points > 0 and player_2.hit_points > 0:
    if player_1_turn:
        selected_attack = input(f"Choose an attack, options are: {player_1.attacks}.")
        if selected_attack in player_1.attacks:
            total = 0
            while total < player_1.attack_quantity[selected_attack]:
                hit.append(random.randint(1,100))
                total += 1
            for roll in hit:
                if roll <= player_1.hit_chance[selected_attack] - player_2.dodge_chance:
                    if selected_attack in mage_attack_names:
                        damage = player_1.damage[selected_attack] + random.randint(1,3) - player_2.magic_defense / 10
                        player_2.hit_points -= damage
                        print(f"You hit for {damage} damage!")
                        player_1_turn = False
                    else:
                        damage = player_1.damage[selected_attack] - player_2.defense / 10
                        player_2.hit_points -= damage
                        print(f"You hit for {damage} damage!")
                        player_1_turn = False
                else:
                    print("Sorry you missed.")
                    player_1_turn = False
            hit = []
            print("Player 2's turn!")
        else:
            print("Invalid attack please choose from the list provided.")
    else:
        selected_attack = input(f"Choose an attack, options are: {player_2.attacks}.")
        if selected_attack in player_2.attacks:
            total = 0
            while total < player_2.attack_quantity[selected_attack]:
                hit.append(random.randint(1,100))
                total += 1
            for roll in hit:
                if roll <= player_2.hit_chance[selected_attack] - player_1.dodge_chance:
                    if selected_attack in mage_attack_names:
                        damage = player_2.damage[selected_attack] +random.randint(1,3) - player_1.magic_defense / 10
                        player_1.hit_points -= damage
                        print(f"You hit for {damage} damage!")
                        player_1_turn = True
                    else:
                        damage = player_2.damage[selected_attack] - player_1.defense / 10
                        player_1.hit_points -= damage
                        print(f"You hit for {damage} damage!")
                        player_1_turn = True
                else:
                    print("Sorry you missed.")
                    player_1_turn = True
            hit = []
            print("Player 1's turn.")
        else:
            print("Invalid attack please choose from the list provided.")

# Winner Decided
if player_1.hit_points <= 0:
    print(f"Player 2 has brutally slain Player 1 with {selected_attack}!")
else:
    print(f"Player 1 has brutally slain Player 2 with {selected_attack}!")