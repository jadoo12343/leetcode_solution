class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        num = list(x**2 for x in nums)
        num.sort()
        n = len(nums)
        total = 0
        left , right = 0 , n - 1
        while left < right :
            total += (num[right] - num[left])
            right -=1
            left +=1
        if n%2==0:
            return total
        else:
            return total + num[n//2]
           

        