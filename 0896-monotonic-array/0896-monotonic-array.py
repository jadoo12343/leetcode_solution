class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sum=0
        diff=0
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                sum+=1
            if nums[i]<=nums[i+1]:
                diff+=1
        return sum==len(nums)-1 or diff==len(nums)-1
            
