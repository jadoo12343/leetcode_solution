class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        for i in range(0, len(s), 2*k):
            reverse = s[i:i+k][::-1]
            unchanged = s[i+k:i+2*k] 
            result += reverse + unchanged
        return result