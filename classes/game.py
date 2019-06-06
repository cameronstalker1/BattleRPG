import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92'
    WARNING = '\033[93'
    FAIL = '\033[91'
    ENDC = '\033[0'
    BOLD = '\033[1'
    UNDERLINE = '\033[4'

class Person:
    def __init__(self, hp, mp, attack, defence, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.attackh = attack + 10
        self.attackl = attack - 10
        self.defence = defence
        self.magic = magic
        self.action = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.attackl, self.attackh)

    def generate_spell_damage(self, i):
        mgl = self.magic[i]["damage"]-5
        mgh = self.magic[i]["damage"]+5
        return random.randrange(mgl, mgh)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp > 0:
            self.hp = 80
        return self.hp
