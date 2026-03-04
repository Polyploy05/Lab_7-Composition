

import random
import math
class Die:
    def __init__(self, sides):
        self.sides = 6
        self.value = 0


    def roll(self):
        self.value = random.randint(1, self.sides)
        return self.value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __eq__ (self, other):
        return self.value == other.value
    
    def __sub__(self, other):
        return abs(self.value - other.value)
    
    def __str__(self):
        return f"Die has a value of {self.value}"
    
