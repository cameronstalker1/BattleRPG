from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


# Create Black Magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 25, 600, "black")
eve = Spell("Eve's pumps", 40, 1400, "black")

# Create White Magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 200, "black")

# Create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("Mega-Elixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, eve, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 5}, {"item": grenade, "quantity": 5}]

# Instantiate Individuals
player1 = Person("Aldo :", 3260, 132, 280, 34, player_spells, player_items)
player2 = Person("Eve  :", 4160, 188, 300, 34, player_spells, player_items)
player3 = Person("Robot:", 3089, 174, 300, 34, player_spells, player_items)

# Instantiate Enemies
enemy = Person("Dragon  ", 1200, 701, 525, 25, [], [])
enemy2 = Person("Dragon 2", 1000, 130, 560, 325, [], [])
enemy3 = Person("Dragon 3", 810, 130, 560, 325, [], [])

players = [player1, player2, player3]
enemies = [enemy, enemy2, enemy3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while running:

    print("\n")
    print("NAME       HP                                    MP")

    for player in players:
        player.get_stats()

    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:

        player.choose_action()
        choice = input("    Choose action")
        index = int(choice) - 1

        if index == 0:

            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("You attacked:", enemies[enemy].name, dmg, "points of damage")

            if enemies[enemy].get_hp() == 0:
                print(bcolors.FAIL + bcolors.BOLD + enemies[enemy].name + " was killed" + bcolors.ENDC)
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic"))-1

            if magic_choice == -1:
                continue

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
                dmg = player.generate_damage()
                enemies[enemy].take_damage(magic_dmg)

                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)

                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to",
                      enemies[enemy].name,  bcolors.ENDC)

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "No items left..." + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name, " heals for",  str(item.prop) + " HP" + bcolors.ENDC)
            elif item.type == "elixer":

                if item.type == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print(bcolors.OKGREEN + "\n" + item.name, " fully restores HP/MP" + bcolors.ENDC)

            elif item.type == "attack":
                enemy.take_damage(item.prop)

                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)

                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), " points of damage to " +
                      enemies[enemy].name + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(bcolors.FAIL + bcolors.BOLD + enemies[enemy].name + " was killed" + bcolors.ENDC)
                    del enemies[enemy]

    enemy_choice = 1

    target = random.randint(0, 3)

    enemy_damage = enemies[0].generate_damage()
    players[target].take_damage(enemy_damage)
    print("Enemy attacks for:", enemy_damage)


# End functionality

    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp() == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp() == 0:
            defeated_players += 1

    if defeated_enemies == 2:
        print(bcolors.OKGREEN, bcolors.BOLD, "YOU WIN", bcolors.ENDC)
        running = False

    elif defeated_players == 2:
        print(bcolors.FAIL, bcolors.BOLD, "Your enemies have defeated you!", bcolors.ENDC)
        running = False
