class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        lo=0
        n=len(nums)
        if nums[0]!=0:
            return 0
        for i in nums:
            if i+1 not in nums:
                return i+1
                

        


        
        