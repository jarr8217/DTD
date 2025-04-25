from characters.base import Character

class Dragon(Character):
    def __init__(self, name):
        super().__init__(name, health=250, attack_power=35)
        self.max_health = 250
        self.fury_cooldown = 0
        self.abilities = ['fire_breath', 'tail_whip', 'dragon_scream', 'dragon_fury']
        self.burn_status = 0
        self.burn_damage = 0  # typo fixed

    def regenerate(self):
        '''Restores a small amount of health, capped by max_health.'''
        old_health = self.health
        self.health = min(self.health + 5, self.max_health)
        recovered = self.health - old_health
        print(f'{self.name} regenerates and restores {recovered} health! Now at {self.health}/{self.max_health} HP.')

    def fire_breath(self, opponent):
        '''Deals damage and applies a burn effect if opponent survives.'''
        damage = self.attack_power + 5
        opponent.take_damage(damage, self.name, "Fire Breath")

        if opponent.health > 0:
            opponent.burn_status = 3
            opponent.burn_damage = 5
            print(f'{opponent.name} is burned for 3 turns!')

    def tail_whip(self, opponent):
        '''Deals normal damage.'''
        damage = self.attack_power
        opponent.take_damage(damage, self.name, "Tail Whip")

    def dragon_scream(self, opponent):
        '''Deals slightly more damage.'''
        damage = self.attack_power + 10
        opponent.take_damage(damage, self.name, "Dragon Scream")

    def dragon_fury(self, opponent):
        '''Deals massive damage but has a cooldown period of 2 turns.'''
        if self.fury_cooldown > 0:
            print(f'{self.name} is on cooldown for Dragon Fury!')
            return False

        damage = self.attack_power + 20
        opponent.take_damage(damage, self.name, "Dragon Fury")
        self.fury_cooldown = 2
        return True

    def reduce_cooldown(self):
        '''Reduces the cooldown for Dragon Fury by 1 turn.'''
        if self.fury_cooldown > 0:
            self.fury_cooldown -= 1

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}, Fury Cooldown: {self.fury_cooldown}")
