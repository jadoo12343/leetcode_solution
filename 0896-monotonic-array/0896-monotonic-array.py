class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True

        inc = True
        dec = True

        for i in range(1, n):
            if not inc and not dec:
                return False

            if nums[i] < nums[i-1]:
                inc = False
            if nums[i] > nums[i-1]:
                dec = False

        return inc or dec
            
