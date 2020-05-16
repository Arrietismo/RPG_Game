from Classes.game import Entity, BColors
from Classes.magic import Spell
from Classes.inventory import Item

# Available black spells.
flame = Spell("Flame", 10, 180, "Dark")
lightning = Spell("Lightning", 12, 1240, "Dark")
blizzard = Spell("Blizzard", 10, 100, "Dark")
quake = Spell("Quake", 15, 1800, "Dark")
meteor = Spell("Meteor", 20, 2500, "Dark")

# Available white spells.
cure = Spell("Cure", 12, 120, "White")
cura = Spell("Cura", 18, 200, "White")

# Items
potion = Item("Potion", "Potion", "Heals 50 HP", 50)
hi_potion = Item("HI Potion", "Potion", "Heals 100 HP", 100)
super_potion = Item("Super potion", "Potion", "Heals 500 HP", 500)
elixir = Item("Elixir", "Potion", "Fully restores HP and MP", 9999)
mega_elixir = Item("Mega Elixir", "Elixir", "Fully restores party members' HP and MP", 9999)
grenade = Item("Grenade", "Weapon", "Deals 500 damage", 500)

player_spells = [flame, lightning, blizzard, meteor, cure]
player_items = [potion, hi_potion, super_potion, elixir, grenade]

# Entities
player = Entity(460, 65, 60, 34, player_spells, player_items)
enemy = Entity(1208, 65, 45, 25, [flame], [])

running = True  # Flag for the on-going battle.
i = 0

print(BColors.FAIL + BColors.BOLD + "AN ENEMY ATTACKS!" + BColors.END_C)

while running:
    print("================")
    # Action Input
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:  # If player attacks
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("Your attacked for ", dmg, " points of damage. " + BColors.FAIL + "Enemy HP: ", enemy.get_hp(), "/",
              enemy.get_max_hp(), BColors.END_C)
    elif index == 1:  # If player uses magic
        # Magic input
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1
        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:  # If there's not enough MP
            print(BColors.FAIL + "Not Enough MP" + BColors.END_C)
            continue

        player.reduce_mp(spell.cost)

        if spell.magic_type == "White":  # Healing magic
            player.heal(magic_dmg)
            print(BColors.OK_BLUE + "HP +", magic_dmg, "! " + BColors.FAIL +
                  "Player HP: ", player.get_hp(), "/", player.get_max_hp())
        else:  # Attack magic
            enemy.take_damage(magic_dmg)
            print(BColors.OK_GREEN + spell.name + " deals ", str(magic_dmg), " points of damage. " + BColors.FAIL +
                  "Enemy HP: ", enemy.get_hp(), "/", enemy.get_max_hp(), BColors.END_C)
    elif index == 2:
        # Item input
        player.choose_item()
        item_choice = int(input("Choose item: ")) - 1
        item = player.inventory[item_choice]

        # TODO Change this to EOF exception.
        if item_choice == -1:
            continue

        if item.type == "Potion":  # If chooses a potion.
            player.heal(item.props)
            print(BColors.OK_GREEN + item.name + " used. Heals for ", item.props, "!" + BColors.END_C)
        elif item.type == "Weapon":  # If chooses a weapon.
            enemy.take_damage(item.props)
            print("You have used " + item.name + ". Deals ", item.props, " to the enemy! " +
                  BColors.FAIL + "Enemy Health: ", enemy.get_hp(), "/", enemy.get_max_hp(), BColors.END_C)

    enemy_choice = 1  # Enemy will always attack

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for ", enemy_dmg, " points of damage. " + BColors.FAIL + "Player HP: ", player.get_hp(), "/",
          player.get_max_hp(), BColors.END_C)

    if enemy.get_hp() == 0:  # If the player isn't dead
        print(BColors.OK_GREEN + "You Win!" + BColors.END_C)
        running = False
    elif player.get_hp() == 0:  # If the player is dead
        print(BColors.FAIL + "You lost..." + BColors.END_C)
        running = False
