class Solution:
    def judgeCircle(self, moves: str) -> bool:
        coordinate=[0,0]
        for direction in moves :
            if direction == "U":
                coordinate[1]+=1
            if direction == "D":
                coordinate[1]-=1
            if direction == "L":
                coordinate[0]-=1
            if direction == "R":
                coordinate[0]+=1
        return coordinate==[0,0]
            

        