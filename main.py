'''
Name:
Date:
Group:
Description:
'''

from player import Player
from check_input import get_yes_no

def take_turn(player):
  
  print("\nRolling dice...")
  player.roll_dice()

  print(player)

  points = 0 

  # Checks if players gets three of a kind
  if player.has_three_of_a_kind():
    print("Three of a kind! +3 points")
    points = 3

  # Only checks series if not three of a kind 
  elif player.has_series():
    print("Series! +2 points")
    points = 2

  # Only check pair iff they scored neither
  elif player.has_pair():
    print("Pair! +1 point")
    points = 1
    
  else:
    print("No combinations this turn.")

  player.points += points

  print(f"Score this turn is completed.")
  print(f"Current score: {player.points}")

def main():
  
  print("Welcome to the Yahtzee!")

  player = Player()

  playing = True
  while playing:
    take_turn(player)
    playing = get_yes_no("\nRoll again? (y/n): ")

  print("\nGame Over!")
  print(f"Final Score: {player.points}")

if __name__ == "__main__":
  main()
