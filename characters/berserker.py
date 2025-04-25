from characters.base import Character

class Berserker(Character):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=30)

    def power_attack(self, opponent):
        damage = self.attack_power
        opponent.health -= damage
        print(f'{self.name} uses Power Attack on {opponent.name} for {damage} damage!')
        if opponent.health <= 0:
            print(f'{opponent.name} has been defeated!')

    def bloodlust(self, opponent):
        damage = self.attack_power * 2
        self.health -= 50
        opponent.health -= damage
        print(f'{self.name} uses Bloodlust on {opponent.name} for {damage} damage!')
        if opponent.health <= 0:
            print(f'{opponent.name} has been defeated!')
        if self.health <= 0:
            print(f'{self.name} has been defeated!')
        
    def life_leech(self, opponent):
        damage = self.attack_power - 10
        self.health += damage
        if self.health > 75:
            self.health = 75
        opponent.health -= damage
        print(f'{self.name} uses Life Leech on {opponent.name} for {damage} damage!')
        if opponent.health <= 0:
            print(f'{opponent.name} has been defeated!')
