from characters.base import Character
from config import BERSERKER_CONFIG

class Berserker(Character):
    '''
    Berserker class representing a powerful berserker character.
    
    Inherits from the Character class and implements specific abilities and behaviors.

    Attributes:
        name (str): The name of the berserker.
        health (int): The current health of the berserker.
        attack_power (int): The base attack power of the berserker.
        max_health (int): The maximum health of the berserker.
        abilities (list): List of abilities available to the berserker.
        calm_mind_used (bool): Flag to check if Calm Mind has been used.
    '''
    def __init__(self, name):
        super().__init__(name, health=BERSERKER_CONFIG['max_health'], attack_power=BERSERKER_CONFIG['attack_power'])
        self.abilities = BERSERKER_CONFIG['abilities']
        self.calm_mind_used = False

    def bloodlust(self, opponent):
        damage = self.attack_power * 2
        self.health -= 35
        opponent.take_damage(damage,self.name, 'Bloodlust')
        if self.health <=0:
            print(f'{self.name} has been defeated from Bloodlust recoil!')
        
    def life_leech(self, opponent):
        damage = self.attack_power - 10
        heal = damage + 10
        opponent.take_damage(damage, self.name, 'Life Leech')
        self.health += heal
        print(f'{self.name} leeches {heal} health from {opponent.name}!')

    def calm_mind(self):
        if self.calm_mind_used:
            print(f'{self.name} has already used Calm Mind!')
            return
        
        heal_amount = self.max_health // 2
        self.health = min(self.max_health, self.health + heal_amount)
        self.calm_mind_used = True

        print(f'{self.name} uses Calm Mind and restores {heal_amount} health! Now at {self.health}/{self.max_health}.')