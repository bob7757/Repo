import random
hit = []
attacks = {"Firebolt": 1, "Magic Missile": 3}
total = 0
attack = input("What attack do you want to use?")
while total < attacks[attack]:
    hit.append(random.randint(1,100))
    total += 1

print(hit)