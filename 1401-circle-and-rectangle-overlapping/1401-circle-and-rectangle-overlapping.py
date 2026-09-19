import math
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        lenght_r = x2 - x1
        height_r = y2 - y1
        xcentre_r = (x1 + x2)/2
        ycentre_r = (y1 + y2)/2
        dbc = math.sqrt((xCenter - xcentre_r)**2 + (yCenter - ycentre_r)**2)
        diagonal_r = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        if xCenter == xcentre_r :
            return True if dbc <= radius + height_r/2 else False
        elif yCenter == ycentre_r :
            return True if dbc <= radius + lenght_r/2 else False
        else:
            return True if dbc <= radius + diagonal_r/2 else False
        