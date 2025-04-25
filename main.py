from gameplay.create_character import create_character
from characters.dragon import Dragon
from gameplay.battle import battle

def main():
    player = create_character()
    dragon = Dragon('The King of Dragons')
    battle(player, dragon)

if __name__ == '__main__':
    main()
