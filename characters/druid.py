from characters.base import Character

class Druid(Character):
    def __init__(self, name):
        super().__init__(name, health=115, attack_power=30)

    def nature_call(self, opponent):
        damage = self.attack_power + 10
        opponent.health -= damage
        print(f'{self.name} calls upon nature to attack {opponent.name} for {damage} damage!')
        if opponent.health <= 0:
            print(f'{opponent.name} has been defeated!')