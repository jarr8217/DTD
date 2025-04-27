def use_item(player):
    '''Allows the player to use an item, such as a healing potion.

    Args:
        player (Character): The player character, an instance of the Character class.
    '''
    if player.healing_potions >0:
        heal_amount = player.max_health // 2
        player.health = min(player.max_health, player.health + heal_amount)
        player.healing_potions -= 1
    else:
        print("You cannot use the item. No healing potions left.")
