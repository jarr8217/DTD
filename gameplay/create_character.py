from characters.warrior import Warrior
from characters.mage import Mage
from characters.berserker import Berserker
from characters.druid import Druid


def create_character():
    print("Choose your character:")
    print("1. Warrior")
    print("2. Mage")
    print('3. Berserker')
    print('4. Druid')

    class_choice = input('Enter the number of your class choice: ')
    name = input('Enter your character name: ')

    if class_choice == '1':
        character = Warrior(name)
    elif class_choice == '2':
        character = Mage(name)
    elif class_choice == '3':
        character = Berserker(name)
    elif class_choice == '4':
        character = Druid(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)
    
    return character
     