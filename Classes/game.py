import random


class BColors:
    """
    Color styles for the command line.
    """
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END_C = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Entity:
    """
        Game's entity
    """
    def __init__(self, hp, mp, atk, df, magic, items):

        """
        :param hp: Entity's health
        :type hp: int

        :param mp: Entity's magic
        :type mp: int

        :param atk: Entity's average attack power
        :type atk: int

        :param magic: Entity's spells
        :type magic: list

        :param items: Entity's items.
        :type items: list
        """
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp  # Stores the maximum health (for the health bar)
        self.mp = mp
        self.atk_low = atk - 10  # Lowest possible attack power
        self.atk_high = atk + 10  # Highest possible attack power
        self.df = df
        self.magic = magic
        self.inventory = items
        self.action = ["Attack", "Magic", "Open Inventory"]

    def generate_damage(self):
        """
        Self-explanatory. Generates a damage between the lowest and the higher.
        :return: Random damage between its lowest and its highest.
        """
        return random.randrange(self.atk_low, self.atk_high)

    def take_damage(self, dmg):
        """
        Inflicts damage to the entity.
        :param dmg: Given damage.
        :return: Current health after being attacked.
        """
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, hp):
        """
        Heals the player lol.
        :param hp: Health points to be added to the entity's current health.
        """
        self.hp += hp

    def get_hp(self):
        """
        Gets current health.
        :return: Current hp
        """
        return self.hp

    def get_max_hp(self):
        """
        Gets entity's initial health.
        :return: Initial hp
        """
        return self.max_hp

    def get_mp(self):
        """
        Gets current magic points
        :return: Current mp.
        """
        return self.mp

    def return_max_mp(self):
        """
        Gets entity's initial magic points.
        :return: Initial mp.
        """
        return self.max_mp

    def reduce_mp(self, cost):
        """
        Subtracts magic points to the entity's mp.
        :param cost: Cost of the spell being used.
        :return: Current mp after using the spell.
        """
        self.mp -= cost
        if self.mp < 0:
            self.mp = 0
        return self.mp

    def choose_action(self):
        """
        Prints the list of available actions.
        """
        index = 1
        for item in self.action:
            print("    " + str(index) + ":", item)
            index += 1

    def choose_magic(self):
        """
        Prints the entity's magic spells.
        :return:
        """
        index = 1
        for spell in self.magic:
            print("    " + str(index) + ":", spell.name, "{cost: ", str(spell.cost) + "}")
            index += 1

    def choose_item(self):
        index = 1
        for item in self.inventory:
            print("    " + str(index) + ". " + item.name + " {Desc: " + item.description + " (x5)}")
            index += 1
