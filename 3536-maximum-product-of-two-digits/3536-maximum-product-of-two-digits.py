class Solution:
    def maxProduct(self, n: int) -> int:
        digits = list(map(int, str(n)))
        if len(digits)==2:
            return digits[0]*digits[1]
        else:
            digits.sort()
            return digits[-1]*digits[-2]
            


        