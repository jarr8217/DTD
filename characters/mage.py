from characters.base import Character

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=30)

    def magic_bullet(self, opponent):
        damage = self.attack_power
        opponent.health -= damage
        print(f'{self.name} casts magic_bullet on {opponent.name} for {damage} damage!')
        if opponent.health <= 0:
            print(f'{opponent.name} has been defeated!') 

    def fireball(self, opponent):
        damage = self.attack_power + 15
        opponent.health -= damage
        print(f'{self.name} casts fireball on {opponent.name} for {damage} damage!')
        if opponent.health <= 0:
            print(f'{opponent.name} has been defeated!')

    def recovery(self):
        old_health = self.health
        self.health = min(self.health + 15, self.max_health)
        recovered = self.health - old_health
        print(f'{self.name} uses recovery and restores {recovered} health! Now at {self.health}/100 HP.')
        if self.health <= 0:
            print(f'{self.name} has been defeated!')
        if self.health > 100:
            self.health = 100
        else:
            print(f'{self.name} is now at {self.health}/100 HP!')

    def arcane_fortify(self):
        if self.has_buffed:
            print(f'{self.name} is already buffed!')
            return
        
        self.max_health += 40
        self.attack_power = max(1, self.attack_power // 2)
        self.health += 20
        
        self.has_buffed = True
        print(f'{self.name} uses Arcane Fortify!')
        print(f'Health increased by 20, max health increased by 40, attack power halved!')
        print(f'{self.name} is now at {self.health}/{self.max_health} HP!')
    