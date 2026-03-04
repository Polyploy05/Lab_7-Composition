


import Die
class Player:
    def __init__(self):
        d1 = Die(6)
        d2 = Die(6)
        d3 = Die(6)
        self.dice = [d1, d2, d3]
        self.points = 0

    def points(self):
        return self.points
    
    def roll_dice(self):
        for die in self.dice:
            die.roll()
    
    def has_pair(self):
        for i in range(len(self.dice)):
            for j in range(i+1, len(self.dice)):
                if self.dice[i] == self.dice[j]:
                    self.points += 1
                    return True
        return False
                
    def has_three_of_a_kind(self):
        if self.dice[0] == self.dice[1] and self.dice[1] == self.dice[2]:
            self.points += 3
            return True
        return False