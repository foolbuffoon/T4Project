# potion health function, repeat function, and main function design by Lilly Pernichele
# import overhead
from character import Character
from location import Location
from monsters import Monster
from spells import Spells
from weapons import Weapons
from consumables import Consumables
import sys

game_start = False
# calling the class objects
player = Character()
locationtest = Location()
monstertest = Monster()
weapontest = Weapons()
spellstest = Spells()
potiontest = Consumables()

ART_LOGO = r"""
 __                               _                 _
/ _\_      ____ _ _ __ ___  _ __ | | __ _ _ __   __| |
\ \\ \ /\ / / _` | '_ ` _ \| '_ \| |/ _` | '_ \ / _` |
_\ \\ V  V / (_| | | | | | | |_) | | (_| | | | | (_| |
\__/ \_/\_/ \__,_|_| |_| |_| .__/|_|\__,_|_| |_|\__,_|
                           |_|
"""
# health potion function
def health_increase(character, consumables):
    if consumables.consume_type == 1:
        character.player_health += 10
        return character.player_health


# main function, contains the gameplay
def main():
    start_input = input("Press enter to begin")
    if start_input == "":
        game_start = True
    start_screen()
    while game_start == True:
        print("You begin your journey...")
        print(
            "You awake in a swamp, with sword in your hand and no idea of who you are in your head"
        )
        end_screen()
        game_start = False
    repeat()


# startscreen/end functions
def start_screen():
    print(ART_LOGO)
    print(
        "Welcome to Swampland, a text-based adventure game made by Lilly Pernichele, Zack Poulson, Liam Scott, and Nikolas Kath \n"
    )
    print(
        "In this game, you will be given a number of choices, each with different outcomes."
    )
    print("To pick a certain option, just type the choice. \n")


def end_screen():
    print(ART_LOGO)
    print("Thank you for playing Swampland!")
    print(
        "This game was developed by Liam Scott, Lilly Pernichele, Nikolas Kath, and Zach Poulson"
    )


# func that allows the user to repeat the game
def repeat():
    end_input = input("Play again? Y/N? ")
    if end_input == "Y" or end_input == "y":
        print("\n")
        main()
    elif end_input == "N" or end_input == "n":
        end_screen()
        sys.exit()


# actually calling the main function.
main()
