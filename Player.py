


import Die
import math

class Player:
    def __init__(self):
        d1 = Die.Die(6)
        d2 = Die.Die(6)
        d3 = Die.Die(6)
        self.dice = [d1, d2, d3]
        self.score = 0

    def points(self):
        return self.score
    
    def roll_dice(self):
        for die in self.dice:
            die.roll()
    
    def has_pair(self):
        for i in range(len(self.dice)):
            for j in range(i+1, len(self.dice)):
                if self.dice[i] == self.dice[j]:
                    self.score += 1
                    return True
        return False
                
    def has_three_of_a_kind(self):
        if self.dice[0] == self.dice[1] and self.dice[1] == self.dice[2]:
            self.score += 3
            return True
        return False
    
    def has_series(self):
        values = sorted([die.value for die in self.dice])
        for i in range(1, len(values)):
            if values[i] != values[i-1] + 1:
                return False
        self.score += 2
        return True
    
    def __str__(self):
        return f"D1: {self.dice[0]}, D2: {self.dice[1]}, D3: {self.dice[2]}"

