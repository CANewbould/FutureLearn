# cat.py

# Version 1

# All cats have nine lives!!

# child of 'Enemy'
# constructor uses parent constructor
# 'attack' uses parent method

from enemy import Enemy

class Cat(Enemy):
    def __init__(self):
        super().__init__(9) # didn't realise that you have to drop 'self'
    def attack(self):
        super().attack("scratch!") # didn't realise that you have to drop 'self'