from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "damage": 60},
         {"name": "Thunder", "cost": 10, "damage": 80},
         {"name": "Blizzard", "cost": 10, "damage": 60},
         {"name": "Eve's pumps", "cost": 10, "damage": 100}]

player = Person(460, 65, 60, 34, magic)

print(player.generate_spell_damage(0))
print(player.generate_spell_damage(1))