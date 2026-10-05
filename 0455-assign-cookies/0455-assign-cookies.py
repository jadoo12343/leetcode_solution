class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        p1 , p2 = 0 , 0
        count = 0
        g.sort()
        s.sort()
        while p2 < len(s) and p1 < len(g):
                if g[p1] <= s[p2]:
                    count +=1
                    p1 +=1
                    p2 +=1
                else:
                    p2 +=1
        return count