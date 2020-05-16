import random


class Spell:
    def __init__(self, name, cost, dmg, magic_type):
        """
        Constructor.
        :param name: Spell's name.
        :type name: str
        :param cost: How much the spell will cost to the entity's magic power.
        :type cost: int
        :param dmg: How much the spell will affect the entity's magic power.
        :type dmg: int
        :param magic_type: Dark (Attack), White (Cure).
        :type magic_type: str
        """
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.magic_type = magic_type

    def generate_damage(self):
        """
        :return: A random damage between the lowest and the highest possible.
        """
        low = self.dmg - 5
        high = self.dmg + 5
        return random.randrange(low, high)
        pass
