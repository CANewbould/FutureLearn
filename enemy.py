# enemy.py

# Version 1

# Brief with a few added features:
# Checks on lives left in both 'attack' and 'checkLife'

class Enemy:
    def __init__ (self):
        self.lives = 3
    def attack(self):
        if self.lives >= 1:
            self.lives -= 1
            print("ouch!")
        else:
            print("No Lives left. ", end = "")
    def checkLife(self):
        if self.lives == 0:
            print("You are dead.")
        elif self.lives == 1:
            print(f'{self.lives} life left')
        else:
            print(f'{self.lives} lives left')

enemy1 = Enemy()
enemy1.attack()
enemy1.checkLife()
enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()
enemy1.attack()
enemy1.checkLife()
enemy2.checkLife()
enemy2.attack()
enemy2.checkLife()
enemy2.attack()
enemy2.checkLife()
enemy2.attack()
enemy2.checkLife()
enemy2.attack()
enemy2.checkLife()
enemy3.attack()
enemy3.checkLife()