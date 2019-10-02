# need to balance damage/defense values to account for combat changes
# player map item?


class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


# Currency
class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold Coins",
                         description="A flat round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)


# consumables
class Consumable(Item):
    def __init__(self, name, description, value, healing):
        self.healing = healing
        super().__init__(name, description, value)

    def __str__(self):
        return "\n=====\n{}\nDescription: {}\nhealing: {}\nValue:  {}".\
            format(self.name, self.description, self.value, self.healing)


# Weapons
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "\n=====\n{}\nDescription: {}\nDamage: {}\nValue: {}".\
            format(self.name, self.description, self.damage, self.value)


# armor
class Armor(Item):
    def __init__(self, name, description, value, defense):
        self.defense = defense
        super().__init__(name, description, value)

    def __str__(self):
        return "\n=====\n{}\nDescription: {}\nDefense: {}\nValue: {}".\
            format(self.name, self.description, self.defense, self.value)


# weapons
class RustySword(Weapon):
    def __init__(self):
        super().__init__(name="Rusty Sword",
                         description="A short sword that is covered in rust.",
                         value=10,
                         damage=5)


class SteelSword(Weapon):
    def __init__(self):
        super().__init__(name="Steel Sword",
                         description="A steel sword that shines dimly. "    
                                     "Stronger than the rusty sword.",
                         value=30,
                         damage=15)


class AstralSilverSword(Weapon):
    def __init__(self):
        super().__init__(name="Astral Silver Sword",
                         description="An elegant astral silver sword, used mainly in monster slaying.",
                         value=50,
                         damage=25)


class RustyAxe(Weapon):
    def __init__(self):
        super().__init__(name="Rusty Axe",
                         description="A dirt covered, rusty axe.",
                         value=10,
                         damage=5)


class BronzeAxe(Weapon):
    def __init__(self):
        super().__init__(name="Bronze Axe",
                         description="A bronze axe with some dents but a strong shaft.",
                         value=30,
                         damage=15)


class MithrilAxe(Weapon):
    def __init__(self):
        super().__init__(name="Mithril Axe",
                         description="A mithril axe, easily capable of taking the head off of a foe.",
                         value=50,
                         damage=25)


class RustyHammer(Weapon):
    def __init__(self):
        super().__init__(name="Rusty Hammer",
                         description="A tarnished, rusty hammer with a splintered hilt.",
                         value=10,
                         damage=5)


class LeadHammer(Weapon):
    def __init__(self):
        super().__init__(name="Lead Hammer",
                         description="An extremely heavy lead hammer with blood still caked on it.",
                         value=30,
                         damage=15)


class AdamantHammer(Weapon):
    def __init__(self):
        super().__init__(name="Adamant Hammer",
                         description="""A special adamant hammer, finely crafted by a master smith. 
                                     Able to crush skulls with ease.""",
                         value=50,
                         damage=25)


class SplinteredBow(Weapon):
    def __init__(self):
        super().__init__(name="Splintered Bow",
                         description="""A rotten looking, splintered bow that can barely shoot straight.""",
                         value=10,
                         damage=5)


class OakBow(Weapon):
    def __init__(self):
        super().__init__(name="Oak Bow",
                         description="""A sturdy bow made of oak with little wear .""",
                         value=50,
                         damage=25)


class YewBow(Weapon):
    def __init__(self):
        super().__init__(name="Yew Bow",
                         description="""An extremely well designed Yew Bow with a powerful enough draw strength to 
                                    pierce any hide.""",
                         value=50,
                         damage=25)


# Armor
class ClothArmor(Armor):
    def __init__(self):
        super().__init__(name="Cloth Armor",
                         description="""A set of tattered cloth armor.""",
                         value=10,
                         defense=.8)


class LeatherArmor(Armor):
    def __init__(self):
        super().__init__(name="Leather Armor",
                         description="""A set of leather armor made from tanned animal hide.""",
                         value=20,
                         defense=.7)


class ChainArmor(Armor):
    def __init__(self):
        super().__init__(name="Chain Armor",
                         description="""A set of chain armor with strong metal rings.""",
                         value=30,
                         defense=.6)


class PlateArmor(Armor):
    def __init__(self):
        super().__init__(name="Plate Armor",
                         description="""A set of plate armor, extremely heavy but gives strong defense""",
                         value=50,
                         defense=.45)


class MithrilArmor(Armor):
    def __init__(self):
        super().__init__(name="Mithril Armor",
                         description="""A set of enchanted mithril armor that can stop even the mightiest of blows.""",
                         value=75,
                         defense=.3)


# consumable items
class CrustyBread(Consumable):
    def __init__(self):
        super().__init__(name="Crusty Bread",
                         description="Old, hard dried bread.  But better than nothing.",
                         healing=10,
                         value=5)


class DirtyWater(Consumable):
    def __init__(self):
        super().__init__(name="Dirty Water",
                         description="Murky water in a canteen.",
                         value=5,
                         healing=10)


class HealingPotion(Consumable):
    def __init__(self):
        super().__init__(name="Healing Potion",
                         description="Heals a moderate amount of HP.",
                         value=25,
                         healing=30)


class LargeHealingPotion(Consumable):
    def __init__(self):
        super().__init__(name="Large Healing Potion",
                         description="Heals a large amount of HP",
                         value=50,
                         healing=60)
