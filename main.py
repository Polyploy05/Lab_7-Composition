'''
Name: Daniel Puerto & Jacob Miranda
Date: 3/4/26
Group: 5 
Description: Creates the full game flow for the Yahtzee game.  Creates the Player object, 
and repeatedly runs turns by calling take_turn until the user chooses to stop. Also uses the 
get_yes_no() to prompt the user to continue or end after each round, and displays the final score
when the game ends.
'''

import Player
from check_input import get_yes_no

def take_turn(player):
  '''
  Plays one turn: rolls dice, displays them and checks whether they win and the types they win. Creates an updated score 
  '''
  print("\nRolling dice...")
  player.roll_dice()

  print(player)

  # Checks if players gets three of a kind
  if player.has_three_of_a_kind():
    print("Three of a kind! +3 points")

  # Only checks series if not three of a kind 
  elif player.has_series():
    print("Series! +2 points")

  # Only check pair if they scored neither
  elif player.has_pair():
    print("Pair! +1 point")
  # Only if there are no points to be added and the die rolls are completed
  else:
    print("No combinations this turn.")

  # Completes turn and shows updated score 
  print(f"Score this turn is completed.")
  print(f"Current score: " + str(player.points()))

def main():
  
  print("Welcome to the Yahtzee!")
  # Creates player 
  player = Player.Player()

  # Game loops 
  playing = True
  while playing:
    take_turn(player)
    playing = get_yes_no("\nRoll again? (y/n): ")

  # Game Ends 
  print("\nGame Over!")
  print(f"Final Score: "+ str(player.points()))

if __name__ == "__main__":
  main()

