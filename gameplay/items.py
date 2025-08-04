def use_item(player):
    '''Allows the player to use an item, such as a healing potion.

    Args:
        player (Character): The player character, an instance of the Character class.
    '''
    if player.healing_potions > 0:
        heal_amount = player.max_health // 2
        player.health = min(player.max_health, player.health + heal_amount)
        player.healing_potions -= 1
        print(f'{player.name} uses a healing potion and restores {heal_amount} health! Now at {player.health}/{player.max_health}. Potions remaining: {player.healing_potions}')
    else:
        print("You cannot use the item. No healing potions left.")
