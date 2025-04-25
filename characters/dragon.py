from characters.base import Character

class Dragon(Character):
    def __init__(self, name):
        super().__init__(name, health=250, attack_power=35)
        self.max_health = 250
        self.fury_cooldown = 0

    def regenerate(self):
        old_health = self.health
        self.health = min(self.health + 5, self.max_health)
        recovered = self.health - old_health
        print(f'{self.name} regenerates and restores {recovered} health! Now at {self.health}/250 HP.')

    def fire_breath(self, opponent):
        damage = self.attack_power + 15
        opponent.health -= damage
        print(f'{self.name} uses Fire Breath on {opponent.name} for {damage} damage!')
        if opponent.health <= 0:
            print(f'{opponent.name} has been defeated!')

    def tail_whip(self, opponent):
        damage = self.attack_power
        opponent.health -= damage
        print(f'{self.name} uses Tail Whip on {opponent.name} for {damage} damage!')
        if opponent.health <= 0:
            print(f'{opponent.name} has been defeated!')  

    def dragon_scream(self, opponent):
        damage = self.attack_power + 5
        opponent.health -= damage
        print(f'{self.name} uses Dragon Scream on {opponent.name} for {damage} damage!')
        if opponent.health <= 0:
            print(f'{opponent.name} has been defeated!')
        
    def dragon_fury(self, opponent):
        if self.fury_cooldown > 0:
            print(f'{self.name} is on cooldown for Dragon Fury!')
            return False
        

        damage = self.attack_power + 20
        opponent.health -= damage
        print(f'{self.name} uses Dragon Fury on {opponent.name} for {damage} damage!')
        if opponent.health <= 0:
            print(f'{opponent.name} has been defeated!')

        self.fury_cooldown = 2
        return True

    def reduce_cooldown(self):
        if self.fury_cooldown > 0:
            self.fury_cooldown -= 1

    def display_stats(self):
        print(f'{self.name}\'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}, Fury Cooldown: {self.fury_cooldown}')
