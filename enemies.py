# enemies.py

# Version 1
# created
# loop used, but doesn't have the flexibility

from enemy import Enemy
from cat import Cat
from trump import Trumpian

enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()

cat1 = Cat()

djt = Trumpian()

enemies = [enemy1, enemy2, enemy3, cat1, djt]

for i in enemies:
    i.attack()
    i.checkLife()

for x in range(0, 4):
    enemy2.attack()
    enemy2.checkLife()
