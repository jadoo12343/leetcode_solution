class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        target = max(nums)
        nums.append(0)
        res = 0
        count = 0
        for i in nums:
            if i == target :
                count +=1
            else:
                res = max(res , count)
                count = 0
        return res