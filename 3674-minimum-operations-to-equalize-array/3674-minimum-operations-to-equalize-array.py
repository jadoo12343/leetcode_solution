class Solution(object):
    def minOperations(self, nums):
        cnt = nums.count(nums[0])
        return 1 if cnt < len(nums) else 0
        