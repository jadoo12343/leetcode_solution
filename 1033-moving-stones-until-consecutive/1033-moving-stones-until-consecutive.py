class Solution:
    def numMovesStones(self, a, b, c):
        maxi = max(a,b,c) - min(a,b,c) - 2
        mini = max((min(abs(a-b),abs(b-c),abs(a-c), 3) - 1), 1)
        if maxi == 0: mini = 0            
        return [mini,maxi]
        