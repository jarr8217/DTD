from characters.base import Character
from config import MAGE_CONFIG

class Mage(Character):
    ''' Mage class representing a powerful mage character.
    
    Inherits from the Character class and implements specific abilities and behaviors.
    
    Attributes:
        name (str): The name of the mage.
        health (int): The current health of the mage.
        attack_power (int): The base attack power of the mage.
        max_health (int): The maximum health of the mage.
        abilities (list): List of abilities available to the mage.
        buffed (bool): Flag to check if Arcane Fortify is active.
    '''
    def __init__(self, name):
        super().__init__(name, health=MAGE_CONFIG['max_health'], attack_power=MAGE_CONFIG['attack_power'])
        self.abilities = MAGE_CONFIG['abilities']
        self.buffed = False
        self.arcane_fortify_cooldown = 0
        self.arcane_fortify_buff_duration = 0

    def magic_bullet(self, opponent):
        damage = self.attack_power
        opponent.take_damage(damage, self.name, 'Magic Bullet')

    def fireball(self, opponent):
        '''Fireball: Deals damage and applies burn status.'''
        damage = self.attack_power - 10
        opponent.take_damage(damage, self.name, 'Fireball')
        if opponent.health > 0:
            opponent.burn_status = 3
            opponent.burn_damage = 5
            print(f'{opponent.name} is burned for 3 turns!')

    def recovery(self):
        heal_amount = 15
        self.health = min(self.max_health, self.health + heal_amount)
        print(f'{self.name} uses Recovery and restores {heal_amount} health! Now at {self.health}/{self.max_health}.')

    def arcane_fortify(self):
        if self.arcane_fortify_buff_duration > 0:
            print(f'{self.name} is already under the effects of Arcane Fortify for {self.arcane_fortify_buff_duration} more turns!')
            return
        
        if not self.buffed:
            self.max_health += 40
            self.attack_power = max(0, self.attack_power // 2)
            self.health = min(self.max_health, self.health + 20)
            self.buffed = True
            self.arcane_fortify_buff_duration = 2
            print(f'{self.name} uses Arcane Fortify! Health increased by 20 and attack power halved for 2 turns!')

        self.arcane_fortify_cooldown = 4

    
    def end_turn(self):
        '''Ends the turn and reduces cooldowns.'''
        if self.buffed:
            self.arcane_fortify_buff_duration -= 1
            if self.arcane_fortify_buff_duration <= 0:
                # Reset the buff effects
                self.max_health -= 40
                self.attack_power = max(0, self.attack_power * 2)
                self.buffed = False
                # Make sure health does not exceed max_health
                if self.health > self.max_health:
                    self.health = self.max_health
                print(f'{self.name}\'s Arcane Fortify buff has worn off! Health and attack power restored to normal.')

        # Handle cooldown
        if self.arcane_fortify_cooldown > 0:
            self.arcane_fortify_cooldown -= 1
            if self.arcane_fortify_cooldown == 0:
                print(f'{self.name}\'s Arcane Fortify is ready to use again!')

