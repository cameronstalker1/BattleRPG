import random
from .magic import Spell


class bcolors:
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    INACTIVE = '\033[90m'
    FAIL = '\033[91m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    OKBLUE = '\033[94m'
    HEADER = '\033[95m'
    COMMENT = '\033[96m'
    BLOCK = '\033[97m'
    CODE = '\033[98m'


class Person:
    def __init__(self, hp, mp, attack, defence, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.attackh = attack + 10
        self.attackl = attack - 10
        self.defence = defence
        self.magic = magic
        self.items = items
        self.action = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.attackl, self.attackh)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1

        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "ACTIONS:" + bcolors.ENDC)
        for item in self.action:
            print("    " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1

        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1

        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print("    " + str(i) + ".", item.name, ":", item.description, " (x5)")
            i += 1

