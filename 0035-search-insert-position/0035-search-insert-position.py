class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        for i in nums:
            if i>=target:
                return nums.index(i)
        return n
            
            
        