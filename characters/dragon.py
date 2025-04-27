from characters.base import Character
from config import DRAGON_CONFIG

class Dragon(Character):
    '''Dragon class representing a powerful dragon character.

    Inherits from the Character class and implements specific abilities and behaviors.

    Attributes:
        name (str): The name of the dragon.
        health (int): The current health of the dragon.
        attack_power (int): The base attack power of the dragon.
        max_health (int): The maximum health of the dragon.
        abilities (list): List of abilities available to the dragon.
        fury_cooldown (int): Cooldown for the Dragon Fury ability.
    
    '''
    def __init__(self, name):
        super().__init__(name, health=DRAGON_CONFIG['max_health'], attack_power=DRAGON_CONFIG['attack_power'])
        self.abilities = DRAGON_CONFIG['abilities']
        self.fury_cooldown = 0


    def regenerate(self):
        heal_amount = 5
        self.health = min(self.max_health, self.health + heal_amount)
        print(f'{self.name} regenerates {heal_amount} health! Now at {self.health}/{self.max_health}.')

    def tail_whip(self, opponent):
        damage = self.attack_power
        opponent.take_damage(damage, self.name, 'Tail Whip')

    def fire_breath(self, opponent):
        damage = self.attack_power - 10
        opponent.take_damage(damage, self.name, 'Fire Breath')
        if opponent.health > 0:
            opponent.burn_status = 3
            opponent.burn_damage = 10
            print(f'{opponent.name} is burned for 3 turns!')

    def dragon_scream(self, opponent):
        damage = self.attack_power + 10
        opponent.take_damage(damage, self.name, 'Dragon Scream')

    def dragon_fury(self, opponent):
        if self.fury_cooldown > 0:
            print(f'{self.name}\'s Dragon Fury is on cooldown for {self.fury_cooldown} more turns!')
            return

        damage = self.attack_power + 20
        opponent.take_damage(damage, self.name, 'Dragon Fury')
        self.fury_cooldown = 3

    def reduce_cooldown(self):
        if self.fury_cooldown > 0:
            self.fury_cooldown -= 1
            

    
        
    