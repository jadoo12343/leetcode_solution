class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n=''.join(sorted(s))
        m=''.join(sorted(t))
        for i in m:
            if s.count(i)!=t.count(i):
                return i
        
        