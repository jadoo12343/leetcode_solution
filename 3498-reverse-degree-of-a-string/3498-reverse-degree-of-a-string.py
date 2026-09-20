class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            val = (123 - ord(s[i]))*( i + 1)
            res += val
        return res

        