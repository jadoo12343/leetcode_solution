class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=0
        y=0
        for direction in moves :
            if direction == "U":
                y+=1
            if direction == "D":
                y-=1
            if direction == "L":
                x-=1
            if direction == "R":
                x+=1
        return x==0 and y==0
            

        