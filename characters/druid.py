from characters.base import Character
from config import DRUID_CONFIG
import random

class Druid(Character):
    '''Druid class representing a powerful druid character.
    
    Inherits from the Character class and implements specific abilities and behaviors.

    Attributes:
        name (str): The name of the druid.
        health (int): The current health of the druid.
        attack_power (int): The base attack power of the druid.
        max_health (int): The maximum health of the druid.
        abilities (list): List of abilities available to the druid.
        bark_skin_cooldown (int): Cooldown for the Bark Skin ability.
        bark_skin_buff_active (bool): Flag to check if Bark Skin is active.
        bark_skin_buff_duration (int): Duration of the Bark Skin buff.
    '''
    def __init__(self, name):
        super().__init__(name, health=DRUID_CONFIG['max_health'], attack_power=DRUID_CONFIG['attack_power'])
        self.abilities = DRUID_CONFIG['abilities']
        self.bark_skin_cooldown = 0
        self.bark_skin_buff_active = False
        self.bark_skin_buff_duration = 0
        self.moonfire_cooldown = 0
        self.original_attack_power = self.attack_power

    def nature_strike(self, opponent):
        damage= self.attack_power
        opponent.take_damage(damage, self.name, 'Nature Strike')
        
    def moonfire(self, opponent):
        '''Moonfire: Deals damage and applies burn status.'''
        if self.moonfire_cooldown > 0:
            print(f'{self.name}\'s Moonfire is on cooldown for {self.moonfire_cooldown} more turns!')
            return
        
        damage = self.attack_power + 10
        opponent.take_damage(damage, self.name, 'Moonfire')

        # Roll for burn effect
        if opponent.health > 0:
            if random.random() < 0.5:
                opponent.burn_status = 3
                opponent.burn_damage = 5
                print(f'{opponent.name} is burned by Moonfire! (3 turns, 5 damage per turn)')
            else:
                print(f'{opponent.name} resists the burn effect!')

        self.moonfire_cooldown = 4

    def healing_touch(self):
        heal_amount = 20 
        self.health = min(self.max_health, self.health + heal_amount)
        print(f'{self.name} uses Healing Touch and restores {heal_amount} health! Now at {self.health}/{self.max_health}.')

    def bark_skin(self):
        if self.bark_skin_cooldown > 0:
            print(f'{self.name}\'s Bark Skin is on cooldown for {self.bark_skin_cooldown} more turns!')
            return

        if not self.bark_skin_buff_active:
            self.max_health += 20
            self.attack_power = max(1, self.attack_power // 2)
            self.health = min(self.max_health, self.health + 10)
            self.bark_skin_buff_active = True
            self.bark_skin_buff_duration = 2
            print(f'{self.name} uses Bark Skin! Health increased by 10 and attack power halved for 2 turns!')

        self.bark_skin_cooldown = 4

    def end_turn(self):
        '''Ends the turn and reduces cooldowns.'''
        if self.bark_skin_buff_active:
            self.bark_skin_buff_duration -= 1
            if self.bark_skin_buff_duration <= 0:
                # Reset the buff effects
                self.max_health -= 20
                self.attack_power = self.original_attack_power
                self.bark_skin_buff_active = False
                # Make sure health does not exceed max_health
                if self.health > self.max_health:
                    self.health = self.max_health
                print(f'{self.name}\'s Bark Skin buff has worn off! Health and attack power restored to normal.')

        # Handle cooldowns
        if self.bark_skin_cooldown > 0:
            self.bark_skin_cooldown -= 1

        if self.moonfire_cooldown > 0:
            self.moonfire_cooldown -= 1
    