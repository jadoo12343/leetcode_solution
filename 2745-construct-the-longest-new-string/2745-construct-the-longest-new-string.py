class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x!=y:
            return (z + min(x,y)*2 + 1)*2
        else:
            return (z + min(x,y)*2)*2
        