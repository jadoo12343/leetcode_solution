class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        res = 0
        n = len(s)
        for i in range(n):
            if s[i] == ')':
                count -=1
                continue
            if s[i] == '(':
                count +=1
            res = max(res , count)
        return res

        