class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        res = []
        for i in range(n):
            if n%(i+1) == 0:
                res.append(nums[i])
        return sum([x**2 for x in res])
