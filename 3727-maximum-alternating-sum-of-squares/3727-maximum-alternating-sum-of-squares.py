class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        num = list(x**2 for x in nums)
        num.sort()
        n = len(nums)
        list1 = num[:n//2]
        list2 = num[n//2:]
        return sum(list2) - sum(list1)
           

        