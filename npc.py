import items


class NonPlayableCharacter:
    def __init__(self, name, gold, inventory):
        self.name = name
        self.gold = gold
        self.inventory = inventory

    def __str__(self):
        return self.name, self.gold, self.inventory


class Trader(NonPlayableCharacter):
    def __init__(self):
        super().__init__(name="Trader",
                         gold=100,
                         inventory=[items.CrustyBread(),
                                    items.CrustyBread(),
                                    items.CrustyBread(),
                                    items.CrustyBread(),
                                    items.HealingPotion(), ])

    def __str__(self):
        return self.name, self.gold, self.inventory

'''class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.gold = 100
        self.inventory = [items.CrustyBread(),
                          items.CrustyBread(),
                          items.CrustyBread(),
                          items.HealingPotion(),
                          items.HealingPotion()]'''