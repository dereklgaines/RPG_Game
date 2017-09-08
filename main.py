from classes.person import person,fonts

magic = [{"spell": "earth","cost":10,"damage":50},
         {"spell": "fire", "cost": 10, "damage": 70},
         {"spell": "wind", "cost": 10, "damage": 60},
         {"spell": "water", "cost": 10, "damage": 40}]

player1 = person("Derek", 300, 100, 60, 30, magic)
enemy1 = person("Goon", 1280, 100, 60, 40, magic)

running = True

print(fonts.BOLD + fonts.FAIL + "An {} has attacked!!!!".format(enemy1.name) + fonts.ENDC)

while running:
    print("=======================")
    player1.choose_action()
    choice = input("Choose Action: ")
    index = int(choice) - 1

    if index == 0:
        damage = player1.generate_damage()
        enemy1.hp -= damage
        print("You attacked for {} points of damage.  The enemy's HP is now {}.".format(damage,enemy1.hp))

    enemy1_choice = 1

    enemy1_damage = enemy1.generate_damage()
    player1.take_damage(enemy1_damage)
    print("You were dealted {} points of damage.  Your HP is now {}.".format(enemy1_damage,player1.get_hp()))
