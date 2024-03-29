import items
import world
import random


class Player:
    def __init__(self):
        self.inventory = [items.RustySword(),
                          items.ClothArmor(),
                          items.CrustyBread(),
                          items.DirtyWater(),
                          ]
        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.hp = 100
        self.gold = 5

    def heal(self):
        consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]
        if not consumables:
            print("You don't have any healing items on you!")
            return

        for i, item in enumerate(consumables, 1):
            print("Choose which item you want to heal with: ")
            print("{}. {}".format(i, item))

# may need to fix self.inventory.remove(to_eat)
        valid = False
        while not valid:
            choice = input()
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("Not a valid healing option, try again.")

    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print("* " + str(item))
        print("Gold: {}".format(self.gold))

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        return best_weapon

    def most_powerful_armor(self):
        max_defense = 0
        best_defense = None
        for item in self.inventory:
            try:
                if item.defense > max_defense:
                    best_defense = item
                    max_defense = item.defense
            except AttributeError:
                pass
        return best_defense

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

# possible formula with enemy defense incorporated.
# enemyhp -= bestwepdmg - enemydefense
# may need to account for negative values
    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        print("You use {} to attack {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You deal {} damage to {}.".format(best_weapon.damage, enemy.name))
            print("You have slain {}!".format(enemy.name))
        else:
            print("{}'s HP is at {}.".format(enemy.name, enemy.hp))
            print("You deal {} damage to {}.".format(best_weapon.damage, enemy.name))

    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)
