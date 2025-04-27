import random

class Character:
    '''Base class for all characters in the game. Handles health, attack, and damage.
    
    Attributes:
        name (str): The name of the character.
        health (int): The current health of the character.
        attack_power (int): The base attack power of the character.
        max_health (int): The maximum health of the character.
        burn_status (int): The number of turns left for burn status.
        burn_damage (int): The damage dealt by burn status each turn.
        abilities (list): List of abilities available to the character.
        healing_potions (int): Number of healing potions available to the character.
    '''


    def __init__(self, name , health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = random.randint(attack_power - 5, attack_power + 5)
        self.max_health = health

        self.burn_status = 0
        self.burn_damage = 0
        self.abilities = []
        self.healing_potions = 2

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        opponent.take_damage(damage, self.name, "Attack")
    
    def take_damage(self, amount, attack_name, ability_name='Attack'):
        self.health -= amount
        print(f'{self.name} takes {amount} damage from {attack_name} using {ability_name}!')
        if self.health <= 0:
            self.health = 0
            print(f'{self.name} has been defeated!')
        else:
            print(f'{self.name} is now at {self.health}/{self.max_health} HP!')

    def burn_damage_effect(self):
        if self.burn_status > 0:
            self.health = max(0, self.health - self.burn_damage)
            print(f'{self.name} is burned and takes {self.burn_damage} damage! Current health: {self.health}/{self.max_health}')
            self.burn_status -= 1
            if self.burn_status == 0:
                print(f'{self.name} is no longer burned!')

    def display_stats(self):
        print(f'Name: {self.name}, Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}')