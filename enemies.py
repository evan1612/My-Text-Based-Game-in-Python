# need to to balance damage/defense values to account for combat changes


class Enemy:
    def __init__(self, name, description, hp, damage, defense):
        self.name = name
        self.description = description
        self.hp = hp
        self.damage = damage
        self.defense = defense

    def is_alive(self):
        return self.hp > 0


class Rat(Enemy):
    def __init__(self):
        super().__init__(name="A Rat",
                         description="A tiny black rat with sharp teeth.",
                         hp=5,
                         damage=1,
                         defense=.8)


class Bat(Enemy):
    def __init__(self):
        super().__init__(name="A Bat",
                         description="A cave bat shrieking loudly.",
                         hp=5,
                         damage=1,
                         defense=.8)


class Slime(Enemy):
    def __init__(self):
        super().__init__(name="A Slime",
                         description="A small blue slime with a gelatinous body.",
                         hp=5,
                         damage=1,
                         defense=.8)


class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="A Goblin",
                         description="A little but evil looking creature with wart covered skin.",
                         hp=10,
                         damage=3,
                         defense=.75)


class Skeleton(Enemy):
    def __init__(self):
        super().__init__(name="A Skeleton",
                         description="A reanimated skeleton with hollow, soul-less eyes",
                         hp=10,
                         damage=3,
                         defense=.75)


class Wolf(Enemy):
    def __init__(self):
        super().__init__(name="A Wolf",
                         description="A large grey wolf with mangy fur.",
                         hp=15,
                         damage=5,
                         defense=.75)


class Spiderling(Enemy):
    def __init__(self):
        super(). __init__(name="A Spiderling",
                          description="A spiderling oozing with venom, "
                                      "it has a bright yellow patch on its thorax",
                          hp=15,
                          damage=5,
                          defense=.75)


class Troll(Enemy):
    def __init__(self):
        super().__init__(name="A Troll",
                         description="A lumbering troll that stands two heads taller than you.",
                         hp=25,
                         damage=9,
                         defense=.65)


class Bear(Enemy):
    def __init__(self):
        super().__init__(name="A Bear",
                         description="A massive grizzly bear with finger sized teeth.",
                         hp=25,
                         damage=9,
                         defense=.65)


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="An Ogre",
                         description="A big fat ogre wielding a club, looking menacingly at you.",
                         hp=35,
                         damage=12,
                         defense=.60)


class Cyclops(Enemy):
    def __init__(self):
        super().__init__(name="An Cyclops",
                         description="A tall cyclops with a single mean eye .",
                         hp=35,
                         damage=12,
                         defense=.60)


class Werewolf(Enemy):
    def __init__(self):
        super().__init__(name="A Werewolf",
                         description="A werewolf with sharp talons and razor like teeth.",
                         hp=40,
                         damage=15,
                         defense=.55)


class Lich(Enemy):
    def __init__(self):
        super().__init__(name="A Lich",
                         description="A master of the undead, able to cast powerful necromancy spells.",
                         hp=40,
                         damage=15,
                         defense=.55)


class RockGolem(Enemy):
    def __init__(self):
        super().__init__(name="A Rock Golem",
                         description="An imposing rock golem, with large granite fists.",
                         hp=50,
                         damage=20,
                         defense=.50)

