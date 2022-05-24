#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Running a simulation with our classes"""

# import our classes
from cheatdice import *

def main():
    """called at runtime"""

    # the player known as the swapper
    jose = duck_cheat()
    # the player known as the loaded_dice
    loaded_dice = Cheat_Loaded_Dice()

    # track scores for both players
    jose_score = 0
    loaded_dice_score = 0

    # how many games we want to run
    number_of_games = 100000
    game_number = 0

    # begin!
    print("Simulation running")
    print("==================")
    while game_number < number_of_games:
        jose.roll()
        loaded_dice.roll()

        jose.cheat()
        loaded_dice.cheat()
        """Remove # before print statements to see simulation running
           Simulation takes approximately one hour to run with print
           statements or ten seconds with print statements
           commented out"""

        #print("Cheater 1 rolled" + str(swapper.get_dice()))
        #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
        if sum(jose.get_dice()) == sum(loaded_dice.get_dice()):
            #print("Draw!")
            pass
        elif sum(jose.get_dice()) > sum(loaded_dice.get_dice()):
            #print("Dice swapper wins!")
            jose_score+= 1
        else:
            #print("Loaded dice wins!")
            loaded_dice_score += 1
        game_number += 1

    # the game has ended
    print("Simulation complete")
    print("-------------------")
    print("Final scores")
    print("------------")
    print(f"Jose won: {jose_score}")
    print(f"Loaded dice won: {loaded_dice_score}")

    # determine the winner
    if jose_score == loaded_dice_score:
        print("Game was drawn")
    elif jose_score > loaded_dice_score:
        print("Jose won most games")
    else:
        print("Loaded dice won most games")

if __name__ == "__main__":
    main()

