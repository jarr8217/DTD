import random

def use_ability(player, ability, target):
    '''Calls the appropriate ability on the player or dragon'''
    if ability in

def battle(player, dragon):
    if not hasattr(player, 'burn_status'):
        player.burn_status = 0
    if not hasattr(dragon, 'burn_status'):
        dragon.burn_status = 0

    while dragon.health > 0 and player.health > 0:
        print('\n--- Your Turn ---')
        print('1. Attack')
        print('2. Use special ability')
        print('3. Heal')
        print('4. View stats')

        choice = input('Choose an action: ')

        if choice == '2':
            abilities = []

            if hasattr(player, 'magic_bullet'):
                abilities.append('magic_bullet')
            if hasattr(player, 'fireball'):
                abilities.append('fireball')
            if hasattr(player, 'recovery'):
                abilities.append('recovery')
            if hasattr(player, 'arcane_fortify'):
                abilities.append('arcane_fortify')

            if not abilities:
                print("No special abilities available.")
            elif len(abilities) == 1:
                ability = abilities[0]
                if ability in ['recovery', 'arcane_fortify']:
                    getattr(player, ability)()
                else:
                    getattr(player, ability)(dragon)
            else:
                print('Choose a special ability:')
                for i, ability in enumerate(abilities, start=1):
                    print(f"{i}. {ability.replace('_', ' ').title()}")
                try:
                    selection = int(input('Enter the number of your choice: '))
                    if 1 <= selection <= len(abilities):
                        ability = abilities[selection - 1]
                        if ability in ['recovery', 'arcane_fortify']:
                            getattr(player, ability)()
                        else:
                            getattr(player, ability)(dragon)
                    else:
                        print("Invalid choice. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == '2':
            player.display_stats()
            dragon.display_stats()
            continue

        else:
            print("Invalid choice. Try again.")
            continue

        # Burn effect on player if applied
        if hasattr(player, 'burn_status') and player.burn_status > 0:
            player.health = max(0, player.health - 5)
            print(f'{player.name} is burned and takes 5 damage!')
            player.burn_status -= 1
            if player.burn_status == 0:
                print(f'{player.name} is no longer burned!')
        if player.health <= 0:
            print(f'{player.name} has been defeated!')
            break

        # Dragon's turn
        if dragon.health > 0:
            dragon.regenerate()
            print("\n--- Dragon's Turn ---")

            actions = ['Fire Breath', 'Tail Whip', 'Dragon Scream']
            if dragon.fury_cooldown == 0:
                actions.append('Dragon Fury')

            dragon_action = random.choice(actions)

            # Execute selected action
            if dragon_action == 'Fire Breath':
                dragon.fire_breath(player)
            elif dragon_action == 'Tail Whip':
                dragon.tail_whip(player)
            elif dragon_action == 'Dragon Scream':
                dragon.dragon_scream(player)
            elif dragon_action == 'Dragon Fury':
                dragon.dragon_fury(player)

            dragon.reduce_cooldown()

            if dragon.burn_status > 0:
                dragon.health = max(0, dragon.health - 5)
                print(f'{dragon.name} is burned and takes 5 damage! Current health: {dragon.health}/{dragon.max_health}')
                dragon.burn_status -= 1
                if dragon.burn_status == 0:
                    print(f'{dragon.name} is no longer burned!')


        if dragon.health <= 0:
            print(f'{dragon.name} has been defeated!')
