class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        res = 0
        for i in range(len(s)):
            if s[i] == ')':
                count -=1
                continue
            if s[i] != '(':
                continue
            count +=1
            res = max(res , count)
        return res

        