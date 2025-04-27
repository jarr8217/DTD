from characters.base import Character
from config import WARRIOR_CONFIG

class Warrior(Character):
    '''Warrior class representing a powerful warrior character.
    
    Inherits from the Character class and implements specific abilities and behaviors.

    Attributes:
        name (str): The name of the warrior.
        health (int): The current health of the warrior.
        attack_power (int): The base attack power of the warrior.
        max_health (int): The maximum health of the warrior.
        abilities (list): List of abilities available to the warrior.
        holy_light_cooldown (int): Cooldown for the Holy Light ability.
        holy_light_buff_active (bool): Flag to check if Holy Light is active.
        original_attack_power (int): The original attack power of the warrior.
    '''
    def __init__(self, name):
        super().__init__(name, health=WARRIOR_CONFIG['max_health'], attack_power=WARRIOR_CONFIG['attack_power'])
        self.abilities = WARRIOR_CONFIG['abilities']
        self.holy_light_cooldown = 0
        self.holy_light_buff_active = False

        self.original_attack_power = self.attack_power  # Store the original attack power

    
    def reave(self, opponent):
        damage = self.attack_power + 10
        opponent.take_damage(damage, self.name, 'Reave')

    def shield(self):
        heal_amount = 20
        self.health = min(self.max_health, self.health + heal_amount)
        print(f'{self.name} uses Shield and restores {heal_amount} health! Now at {self.health}/{self.max_health}.')

        
        
    def holy_light(self, opponent):
        if self.holy_light_cooldown > 0:
            print(f'{self.name}\' is on cooldown for {self.holy_light_cooldown} more turns!')
            return
        
        heal_amount = 25
        self.health = min(self.max_health, self.health + heal_amount)
        self.attack_power += 15
        self.holy_light_buff_active = True
        self.holy_light_cooldown = 3

        print(f'{self.name} uses Holy Light! Restores {heal_amount} health and gains +15 attack power!')

    def end_turn(self):
        '''Ends the turn and reduces cooldowns.'''
        if self.holy_light_cooldown > 0:
            self.holy_light_cooldown -= 1

        if self.holy_light_buff_active and self.holy_light_cooldown == 0:
            self.attack_power = self.original_attack_power
            self.holy_light_buff_active = False
            print(f'{self.name}\'s Holy Light buff has worn off! Attack power restored to normal.')
        
