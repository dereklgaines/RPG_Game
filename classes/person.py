import random

# Creates background colors for the game
class fonts:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Creates players or enemies
class person:
    def __init__(self,name,hp,mp,atk,df,magic):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack","Magic"]

    # Calculates damage for normal attacks
    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)

    # Calculates damage for magic spells
    def generate_magic_damage(self,index):
        magicl = self.magic[index]["damage"] - 5
        magich = self.magic[index]["damage"] + 5
        return random.randrange(magicl,magich)

    # Takes damage from normal attacks and magic
    def take_damage(self,damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp

    # Returns the HP of players and enemies
    def get_hp(self):
        return self.hp

    # Returns the maximum HP of players and enemies
    def get_maxhp(self):
        return self.maxhp

    # Reduce magic points
    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self,cost):
        self.mp -= cost

    def get_spell_name(self,index):
        return self.magic[index]["spell"]

    def get_spell_mp_cost(self,index):
        return self.magic[index]["cost"]

    def choose_action(self):
        i = 1
        print("\n" + fonts.OKBLUE + fonts.BOLD + "Actions" + fonts.ENDC)
        for item in self.actions:
            print("   ",str(i) , ":", item)
            i += 1


    def choose_spell(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(str(i) + ":", spell["spell"],"(cost:",str(spell["cost"]) + ")")
            i += 1



