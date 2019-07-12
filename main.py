from classes.game import Person, bcolors
from classes.magic import Spell

# Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 10, 100, "black")
quake = Spell("Quake", 10, 100, "black")
eve = Spell("Eve's pumps", 10, 100, "black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "black")

#Instantiate Individuals
player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, quake, eve, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    print("==========================")
    player.choose_action()
    choice = input("Choose action")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for:", dmg, "points of damage, enemy hp:", enemy.get_hp())

    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic"))-1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + bcolors.BOLD + "\nNOT ENOUGH MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for,", str(magic_dmg), "HP.", bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage", bcolors.ENDC)

    enemy_choice = 1

    enemy_damage = enemy.generate_damage()
    player.take_damage(enemy_damage)
    print("Enemy attacks for:", enemy_damage)

    print("==========================")
    print("Enemy hp:", bcolors.FAIL, str(enemy.get_hp()), "/", str(enemy.get_maxhp()), bcolors.ENDC + "\n")
    print("Your hp:", bcolors.OKGREEN, str(player.get_hp()), "/", str(player.get_maxhp()), bcolors.ENDC)
    print("Your mp:", bcolors.OKBLUE, str(player.get_mp()), "/", str(player.get_maxmp()), bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN, bcolors.BOLD, "YOU WIN", bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL, bcolors.BOLD, "YOU DIED", bcolors.ENDC)
        running = False



