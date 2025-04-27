from gameplay.create_character import create_character
from characters.dragon import Dragon
from gameplay.battle import battle

def main():
    '''Main function to start the game. It initializes the player and dragon characters, and starts the battle.'''
    print('====================================')
    print('Welcome to the VS Dragon Game!')
    print('You will face the mighty Dragon in a battle of wits and strength.')
    print('====================================')
    player = create_character()
    dragon = Dragon('Dragun, the Dragon King')
    battle(player, dragon)

if __name__ == '__main__':
    main()
