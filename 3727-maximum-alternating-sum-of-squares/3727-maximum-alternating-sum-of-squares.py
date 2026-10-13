class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        num = list(x**2 for x in nums)
        num.sort()
        n = len(nums)
        return sum(num[n//2:]) - sum(num[:n//2]) 
           

        