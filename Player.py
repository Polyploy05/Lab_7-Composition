


from die import Die
class Player:
    def __init__(self):
        d1 = Die(6)
        d2 = Die(6)
        d3 = Die(6)
        self._dice = [d1, d2, d3]
        self._dice.sort()
        self._points = 0

    @property
    def points(self):
        return self._points
    
    def roll_dice(self):
        for die in self._dice:
            die.roll()
        self._dice.sort()
    
    def has_pair(self):
        if self._dice[0] == self._dice[1] or self._dice[1] == self._dice[2]:
            self._points += 1
            return True
        return False
                
    def has_three_of_a_kind(self):
        if self._dice[0] == self._dice[1] and self._dice[1] == self._dice[2]:
            self._points += 3
            return True
        return False

    def has_series(self):
        v1 = self._dice[0].value
        v2 = self._dice[1].value
        v3 = self._dice[2].value

        if v2 - v1 == 1 and v3 - v2 == 1:
            self._points += 2
            return True
        return False

    def __str__(self):
        return f"D1 = {self._dice[0].value}, D2 = {self._dice[1].value}, D3 = {self._dice[2].value}"

