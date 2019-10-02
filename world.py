import enemies
import random
import npc
import player


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass


class StartTile(MapTile):
    def intro_text(self):
        return """
        You find yourself at a crossroads of sorts.  North leads to snowy tundras, West leads to a long mountain range, 
        East leads to an enchanting forest, and South leads you to a barren desert.
        """


# low level enemy spawn tile?
class EnemyTile(MapTile):
    def __init__(self, x, y):
        self.player = player
        r = random.random()
        if r < 0.25:
            self.enemy = enemies.Bat()
            self.alive_text = "A bat swoops in on you out of nowhere."
            self.dead_text = "The body of a bat lies still on the ground"
        elif r < 0.50:
            self.enemy = enemies.Rat()
            self.alive_text = "A rat screeches and lunges at you."
            self.dead_text = "The dead body of a rat lies here."
        elif r < 0.75:
            self.enemy = enemies.Slime()
            self.alive_text = "A slime rolls towards you leaving an oozing trail."
            self.dead_text = "A slime lies dead here in a puddle of goo."
        else:
            self.enemy = enemies.Goblin()
            self.alive_text = "a goblin swinging a small branch scurries towards you."
            self.dead_text = "The bloody corpse of a goblin lies still."

        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

# possible working damage formula with player defense incorporated.
# playerhp = playerhp - (enemydmg - bestarmor)
# may need to account for negative values
    def modify_player(self, player):
        best_armor = player.most_powerful_armor()
        enemy_dmg = self.enemy.damage * best_armor.defense
        if self.enemy.is_alive():
            player.hp = round(player.hp) - round(enemy_dmg)
            print("{} does {} damage.  You have {} HP remaining.".
                  format(self.enemy.name, self.enemy.damage, player.hp))


class VictoryTile(MapTile):
    def intro_text(self):
        return """
        You've done it!...
        
        ...Victory is yours!
        """


class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1, 25)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return"""
            Nothing more to find here, keep moving.
            """
        else:
            return"""
            There is some gold on the ground, you take it.
            """

# make sure im calling from the right inventory list!!!
class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ['Q', 'q']:
                return
            elif user_input in ['B', 'b']:
                print("Here's whats available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ['S', 's']:
                print("Here's whats available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")

    def trade(self, seller, buyer):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ['Q', 'q']:
                return
            else:
                try:
                    choice = int(user_input)
                    print('User choice: ' + str(choice)) #  debug print
                    print('User choice - 1: ' + str(choice - 1)) #  debug print
                    print('Size of list: ' + str(len(seller.inventory))) #  debug print
                    to_swap = seller.inventory[choice - 1]
                    print("to swap: " + str(to_swap)) #  debug print
                    self.swap(seller, buyer, to_swap)
                    print("self.swap: " + str(self.swap(seller, buyer, to_swap))) #  debug print
                except ValueError:
                    print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        print("seller.inventory.remove(item) = " + seller.inventory.remove(item)) #  debug print
        buyer.inventory.append(item)
        print("buyer.inventory.append(item) = " + buyer.inventory.append(item)) #  debug print
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("seller.gold " + seller.gold) #  debug print
        print("buyer.gold " + buyer.gold)  #  debug print
        print("Trade complete!")

    def intro_text(self):
        return """
        A frail not-quite-human, not-quite-creature squats in the corner
        clinking his gold coins together. He looks willing to trade.
        """


# ST = start tile
# VT = victory tile
# VT = enemy tile
# FG = Gold tile
# TT = Trader tile
world_dsl = """
|EN|EN|VT|  |TT|
|FG|EN|  |FG|EN|
|EN|  |TT|EN|FG|
|EN|  |ST|  |EN|
|TT|FG|TT|FG|EN|
"""


def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True


tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "FG": FindGoldTile,
                  "TT": TraderTile,
                  "  ": None}

world_map = []

start_tile_location = None


def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
