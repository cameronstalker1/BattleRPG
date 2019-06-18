from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "damage": 100},
         {"name": "Thunder", "cost": 10, "damage": 124},
         {"name": "Blizzard", "cost": 10, "damage": 100},
         {"name": "Eve's pumps", "cost": 10, "damage": 300}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

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
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + bcolors.BOLD + "\nNOT ENOUGH MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell + "deals", str(magic_dmg), "points of damage", bcolors.ENDC)

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



