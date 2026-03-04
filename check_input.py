import check_input
import random

'''Authors: Jacob Miranda, Justin Hahn, Daniel Puerto
Date: 1/21/2026
Function: Plays a shell game with the user where they can bet money on guessing
the position of a ball under one of three shells. Runs until the user runs out of money
or chooses to stop playing.'''

def main():

    """Sets up the initial variables for amount of money to spend, as well as a
    placeholder variable for the bet amount and the continuation criteria"""
    wallet = 100
    bet = int(-1)
    play = True
    print("-Shell Game-")
    print("Find the ball to double your bet!")
    print("")

    """Main loop sequence. Obtains a bet amount, randomizes the ball position,
    shows the cups, and obtains the user's guess."""
    while play:
        print(f"You have $" + str(wallet) + " to play with.")
        bet = check_input.get_int_range("Please Enter your bet: ", 1, int(wallet))
        ball_position = random.randint(1, 3)
        print("  _____       _____       _____ ")
        print(" /     \\     /     \\     /     \\")
        print("/   1   \\   /   2   \\   /   3   \\")
        print("---------   ---------   ---------")

        guess = check_input.get_int_range("Guess the shell (1-3): ", 1, 3)


        """Shows the position of the ball after the user's guess."""
        if ball_position == 1:
            print("  _____       _____       _____ ")
            print(" /     \\     /     \\     /     \\")
            print("/   o   \\   /      \\   /      \\")
            print("---------   ---------   ---------")
        elif ball_position == 2:
            print("  _____       _____       _____ ")
            print(" /     \\     /     \\     /     \\")
            print("/       \\   /   o   \\   /       \\")
            print("---------   ---------   ---------")
        else:
            print("  _____       _____       _____ ")
            print(" /     \\     /     \\     /     \\")
            print("/       \\   /       \\   /   o   \\")
            print("---------   ---------   ---------")

        """Adds money to the wallet if the user guesses correctly, subtracts otherwise.
        Tells the user of the outcome then asks if they want to play again."""
        if guess == ball_position:
            wallet += bet
            print(f"Congragulations!")
        else:
            wallet -= bet
            print(f"Sorry, you lost.")

        """Two checks for continuation: if the user is out of money, or if they choose not to continue."""
        if wallet<= 0:
            print("You have run out of money to play.")
            break
        play = check_input.get_yes_no("Do you want to play again? (y/n): ")
        
    print("Thanks for playing!")
    
main()