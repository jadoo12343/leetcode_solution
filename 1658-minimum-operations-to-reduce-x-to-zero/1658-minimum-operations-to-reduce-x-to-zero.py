class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        n = len(nums)
        if target < 0 :
            return -1
        elif target ==0:
            return n
        res = -1 
        currsum = 0
        j = 0
        for i in range(n):
            currsum += nums[i]
            while currsum > target:
                currsum -= nums[j]
                j +=1
            if currsum == target:
                res = max(res , (i - j +1))
        return n - res if res != -1 else -1