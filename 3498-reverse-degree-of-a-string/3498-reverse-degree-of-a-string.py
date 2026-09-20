class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            val = (123 - ord(s[i]))*( i + 1)
            res += val
        return res

        