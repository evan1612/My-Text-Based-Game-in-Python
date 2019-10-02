# My-Text-Based-Game-in-Python
trade method bugged?

Notes:
1) Able to buy all and sell all items in list if I do 1 by 1, using quit command after each trade.
2) Using a number that isn't on list causes the same error to occur.


error recieved:

Traceback (most recent call last):
  File "C:/Users/Evan/OneDrive/Documents/Text Game V2/game.py", line 60, in <module>
    play()
  File "C:/Users/Evan/OneDrive/Documents/Text Game V2/game.py", line 15, in play
    choose_action(room, player)
  File "C:/Users/Evan/OneDrive/Documents/Text Game V2/game.py", line 25, in choose_action
    action()
  File "C:\Users\Evan\OneDrive\Documents\Text Game V2\player.py", line 105, in trade
    room.check_if_trade(self)
  File "C:\Users\Evan\OneDrive\Documents\Text Game V2\world.py", line 115, in check_if_trade
    self.trade(buyer=self.trader, seller=player)
  File "C:\Users\Evan\OneDrive\Documents\Text Game V2\world.py", line 132, in trade
    to_swap = seller.inventory[choice - 1]
IndexError: list index out of range
