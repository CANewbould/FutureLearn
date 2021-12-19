# enemy.py

# Version 2

# added a default value to the constructor
# changed 'attack' to have  different messages for different classes, with default

class Enemy:
    def __init__ (self, lives = 3):
        self.lives = lives
    def attack(self, message = "ouch!"):
        if self.lives >= 1:
            self.lives -= 1
            print(message)
        else:
            print("No Lives left. ", end = "")
    def checkLife(self):
        if self.lives == 0:
            print("You are dead.")
        elif self.lives == 1:
            print(f'{self.lives} life left')
        else:
            print(f'{self.lives} lives left')
