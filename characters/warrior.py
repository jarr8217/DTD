from characters.base import Character

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=20)
        self.abilities = ['power_attack', 'reave', 'shield', 'holy_light']

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
        self.health = min(self.health +10, self.max_health)
        print(f'{self.name} uses Shield and restores 10 health! Now at {self.health}/{self.max_health}.')
        
        
    def holy_light(self):
        old_health = self.health
        self.health = min(self.health + 25, self.max_health)
        recovered = self.health - old_health
        print(f'{self.name} uses recovery and restores {recovered} health! Now at {self.health}/{self.max_health}.')