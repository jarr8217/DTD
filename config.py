'''
This module contains the configuration for different character classes in a game.
It defines the maximum health, attack power, and abilities for each character type.
'''

WARRIOR_CONFIG = {
    'max_health': 170,
    'attack_power': 30,
    'abilities': ['reave', 'shield', 'holy_light'],
}

BERSERKER_CONFIG = {
    'max_health': 150,
    'attack_power': 30,
    'abilities': ['bloodlust', 'life_leech', 'calm_mind'],
}

DRAGON_CONFIG = {
    'max_health': 221,
    'attack_power': 25,
    'abilities': ['fire_breath', 'tail_whip', 'dragon_scream', 'dragon_fury'],
}

MAGE_CONFIG = {
    'max_health': 145,
    'attack_power': 30,
    'abilities': ['magic_bullet', 'fireball', 'recovery', 'arcane_fortify'],
}

DRUID_CONFIG = {
    'max_health': 155,
    'attack_power': 25,
    'abilities': ['nature_strike', 'moonfire', 'healing_touch', 'bark_skin'],
}
