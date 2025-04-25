from characters.base import Character

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=20)

    def power_attack(self, opponent):
        damage = self.attack_power
        opponent.health -= damage
        print(f'{self.name} uses Power Attack on {opponent.name} for {damage} damage!')
        if opponent.health <= 0:
            print(f'{opponent.name} has been defeated!')
    
    def reave(self, opponent):
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f'{self.name} uses Reave on {opponent.name} for {damage} damage!')
        if opponent.health <= 0:
            print(f'{opponent.name} has been defeated!')

    def shield(self):
        self.health += 10
        print(f'{self.name} uses Shield to gain 10 health!')
        if self.health > 140:
            self.health = 140
        else:
            print(f'{self.name} is now at {self.health}/140 HP!')
        