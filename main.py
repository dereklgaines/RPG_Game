from classes.person import person,fonts
from classes.magic import spell

# Create Black Magic
earth = spell("Earth",10,100,"black")
fire = spell("Fire",10,100,"black")
wind = spell("Wind",10,100,"black")
water = spell("Water",10,100,"black")
electricity = spell("Electicity",10,100,"black")

# Create White Magic
potion = spell("Potion",10,100,"white")
elixir = spell("Elixir",10,100,"white")

magic = [earth, fire, wind, water, electricity, potion, elixir]

player1 = person("Derek", 300, 100, 60, 30, magic)
enemy1 = person("Goon", 1280, 100, 60, 40, magic)

running = True

print(fonts.BOLD + fonts.FAIL + "A {} has attacked!!!!".format(enemy1.get_name()) + fonts.ENDC)

while running:
    print("=======================")
    player1.choose_action()
    choice = int(input("Choose Action: ")) - 1

    if choice == 0:
        damage = player1.generate_damage()
        enemy1.hp -= damage
        print("\nYou attacked for {} points of damage.".format(damage))
    elif choice == 1:
        player1.choose_spell()
        magic_choice = int(input("Choose Spell: ")) - 1
        spell = player1.magic[magic_choice]
        cost = spell.cost
        print("\nYou chose " + fonts.FAIL + spell.name + fonts.ENDC)
        hp_mod = spell.generate_damage(spell)

        if cost > player1.get_mp():
            print(fonts.WARNING, "\nYou do not have enough MP!!", fonts.ENDC)
            continue

        player1.mp -= cost

        if spell.type == "black":
            enemy1.hp -= hp_mod
            print("\nYour {} spell did {} points of damage.".format(spell.name,hp_mod))
        elif spell.type == "white":
            player1.heal_hp(spell.damage)

    enemy1_choice = 1

    enemy1_damage = enemy1.generate_damage()
    player1.take_damage(enemy1_damage)
    print("You were dealted {} points of damage.".format(enemy1_damage))

    print("\n=======================")

    print("{}'s HP: {}/{}".format(enemy1.name, enemy1.get_hp(), enemy1.get_maxhp()) + "\n")

    print("{}'s HP: {}/{}".format(player1.name, player1.get_hp(), player1.get_maxhp()),"MP: {}/{}".format(player1.get_mp(),player1.get_maxmp()))

    if enemy1.get_hp() == 0:
        print(fonts.OKGREEN + "You have defeated {}!!!!".format(enemy1.name) + fonts.ENDC)
        running = False
    if player1.get_hp() <= 100:
        print(fonts.WARNING + "Your health is low. Please heal yourself." + fonts.ENDC)
        if player1.get_hp() == 0:
            print(fonts.FAIL + "You have been defeated :(" + fonts.ENDC)
            running = False
