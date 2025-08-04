def use_ability(player, opponent=None):
    '''
    Allows the player to choose a special ability to use against the opponent.

    Args:
        player (Character): The player character, an instance of the Character class.
        opponent (Character): The opponent character, an instance of the Character class.
    '''
    if not hasattr(player, 'abilities') or not player.abilities:
        print(f"{player.name} has no special abilities!")
        return

    print("\nChoose a special ability:")
    for idx, ability in enumerate(player.abilities, 1):
        print(f"{idx}. {ability.replace('_', ' ').title()}")

    try:
        selection = int(input('Enter the number of your choice: '))
        if 1 <= selection <= len(player.abilities):
            ability_name = player.abilities[selection - 1]
            ability_method = getattr(player, ability_name)
            # Determine if the ability needs a target (heal abilities usually don't)
            if any(keyword in ability_name for keyword in ["heal", "shield", "bark", "recovery", "holy_light", "calm_mind", "healing_touch", "arcane_fortify"]):
                ability_method()
            else:
                ability_method(opponent)
        else:
            print("Invalid ability choice.")
    except ValueError:
        print("Invalid input. Please try again.")
