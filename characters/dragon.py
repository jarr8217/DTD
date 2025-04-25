from characters.base import Character

class Dragon(Character):
    def __init__(self, name):
        super().__init__(name, health=250, attack_power=35)
        self.max_health = 250
        self.fury_cooldown = 0

    def regenerate(self):
        '''Restores a small amount of health, capped by max_health.'''
        old_health = self.health
        self.health = min(self.health + 5, self.max_health)
        recovered = self.health - old_health
        print(f'{self.name} regenerates and restores {recovered} health! Now at {self.health}/250 HP.')

    def fire_breath(self, opponent):
        '''Deals damage and applies a burn effect for 3 turns.'''
        damage = self.attack_power + 5
        opponent.health = max(0, opponent.health - damage) #Prevents negative health
        print(f'{self.name} uses Fire Breath on {opponent.name} for {damage} damage!')
        if opponent.health == 0:
            print(f'{opponent.name} has been defeated!')
        else:
            # Burn effect
            opponent.burn_status = 3
            print(f'{opponent.name} is burned for 3 turns!')
            opponent.burn_damage = 5

    def tail_whip(self, opponent):
        damage = self.attack_power
        opponent.health = max(0, opponent.health - damage)
        print(f'{self.name} uses Tail Whip on {opponent.name} for {damage} damage!')
        if opponent.health == 0:
            print(f'{opponent.name} has been defeated!')  

    def dragon_scream(self, opponent):
        damage = self.attack_power + 5
        opponent.health = max(0, opponent.health - damage)
        print(f'{self.name} uses Dragon Scream on {opponent.name} for {damage} damage!')
        if opponent.health == 0:
            print(f'{opponent.name} has been defeated!')
        
    def dragon_fury(self, opponent):
        '''Deals massive damage but has a cooldown period of 2 turns.'''
        if self.fury_cooldown > 0:
            print(f'{self.name} is on cooldown for Dragon Fury!')
            return False
        

        damage = self.attack_power + 20
        opponent.health = max(0, opponent.health - damage)
        print(f'{self.name} uses Dragon Fury on {opponent.name} for {damage} damage!')
        if opponent.health == 0:
            print(f'{opponent.name} has been defeated!')

        self.fury_cooldown = 2 # start cooldown after using Dragon Fury
        return True

    def reduce_cooldown(self):
        '''Reduces the cooldown for Dragon Fury by 1.'''
        if self.fury_cooldown > 0:
            self.fury_cooldown -= 1

    def display_stats(self):
        print(f'{self.name}\'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}, Fury Cooldown: {self.fury_cooldown}')
