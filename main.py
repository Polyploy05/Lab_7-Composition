'''
Name:
Date:
Group:
Description:
'''

import Player
from check_input import get_yes_no

def take_turn(player):
  
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
    
  else:
    print("No combinations this turn.")


  print(f"Score this turn is completed.")
  print(f"Current score: " + str(player.points()))

def main():
  
  print("Welcome to the Yahtzee!")

  player = Player.Player()

  playing = True
  while playing:
    take_turn(player)
    playing = get_yes_no("\nRoll again? (y/n): ")

  print("\nGame Over!")
  print(f"Final Score: "+ str(player.points()))

if __name__ == "__main__":
  main()
