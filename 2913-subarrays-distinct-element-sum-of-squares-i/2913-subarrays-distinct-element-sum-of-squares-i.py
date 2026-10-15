class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = []
        count = 0

        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                res.append(nums[i : j + 1])
        
        for i in range(len(res)):
            count += (len(set(res[i])))**2
        return count