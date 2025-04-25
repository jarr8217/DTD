import random

def battle(player, dragon):
    while dragon.health > 0 and player.health > 0:
        print('\n--- Your Turn ---')
        print('1. Attack')
        print('2. Use special ability')
        print('3. Heal (not yet implemented)')
        print('4. View stats')

        choice = input('Choose an action: ')

        if choice == '1':
            player.attack(dragon)

        elif choice == '2':
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

        elif choice == '3':
            print("Healing is not yet implemented.")

        elif choice == '4':
            player.display_stats()
            dragon.display_stats()
            continue

        else:
            print("Invalid choice. Try again.")
            continue

        if player.health <= 0:
            print(f'{player.name} has been defeated!')
            break

        # Dragon's turn
        if dragon.health > 0:
            dragon.regenerate()

            print("\n--- Dragon's Turn ---")
            print("Choose dragon's attack:")
            print("1. Fire Breath")
            print("2. Tail Whip")
            print("3. Dragon Scream")
            if dragon.fury_cooldown == 0:
                print("4. Dragon Fury (Ready)")
            else:
                print(f"4. Dragon Fury (Cooldown: {dragon.fury_cooldown} turn(s) remaining)")

            dragon_choice = input("Enter the number of the dragon's attack: ")

            if dragon_choice == '1':
                dragon.fire_breath(player)
            elif dragon_choice == '2':
                dragon.tail_whip(player)
            elif dragon_choice == '3':
                dragon.dragon_scream(player)
            elif dragon_choice == '4':
                if dragon.fury_cooldown == 0:
                    dragon.dragon_fury(player)
                else:
                    print("Dragon Fury is on cooldown! Turn skipped.")
            else:
                print("Invalid choice. Dragon does nothing this turn.")

            dragon.reduce_cooldown()

        if dragon.health <= 0:
            print(f'{dragon.name} has been defeated!')
