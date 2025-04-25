from gameplay.create_character import create_character
from characters.dragon import Dragon
from gameplay.battle import battle

def main():
    print('Welcome to the VS Dragon Game!')
    print('You will face the mighty Dragon in a battle of wits and strength.')
    player = create_character()
    dragon = Dragon('The King of Dragons')
    battle(player, dragon)

if __name__ == '__main__':
    main()
