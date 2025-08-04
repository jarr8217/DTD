import random
from gameplay.items import use_item
from gameplay.use_abilities import use_ability


def battle(player, dragon):
    '''
    Executes the turn-based battle between the player and the dragon.

    this function manages the flow of the battle, alternating turns between the player and the dragon.
    The player can choose actions such as attacking, using abilities, using items, or viewing stats.
    The dragon regenerates health and uses its abilities to attack the player. The battle ends when 
    either the player or the dragon's health reaches zero.

    Args:
        player (Character): The player character, an instance of the Character class.
        dragon (Dragon): The dragon character, an instance of the Dragon class.    
    '''
    if not hasattr(player, 'burn_status'):
        player.burn_status = 0
    if not hasattr(player, 'burn_damage'):
        player.burn_damage = 0

    while player.health > 0 and dragon.health > 0:
        print(f'\n--- Your Turn ---')
        print('1. Attack')
        print('2. Use Ability')
        print('3. Use Item')
        print('4. View Stats')

        choice = input('Choose an action: ')

        if choice == '1':
            player.attack(dragon)
        elif choice == '2':
            use_ability(player, dragon)
        elif choice == '3':
            use_item(player)
        elif choice == '4':
            player.display_stats()
            dragon.display_stats()
            continue
        else:
            print('Invalid choice. Try again.')
            continue

        # Handle burn damage after player's turn
        player.burn_damage_effect()
        dragon.burn_damage_effect()

        if dragon.health <= 0:
            print(f'Congratulations! You defeated {dragon.name}!')
            break
        if player.health <= 0:
            print(f'{player.name} has been defeated!')
            break
        if hasattr(player, 'end_turn'):
            player.end_turn()

        # Dragon's Turn
        print(f'\n--- {dragon.name}\'s Turn ---')
        dragon.regenerate()

        dragon_actions = ['fire_breath', 'tail_whip', 'dragon_scream']
        if dragon.fury_cooldown == 0:
            dragon_actions.append('dragon_fury')

        dragon_move = random.choice(dragon_actions)
        getattr(dragon, dragon_move)(player)
        dragon.reduce_cooldown()

        # Handle burn damage again after dragon's turn
        player.burn_damage_effect()
        dragon.burn_damage_effect()
