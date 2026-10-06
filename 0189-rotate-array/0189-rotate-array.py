class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if k > n:
            k = k%n
        i = n - k
        l1 = nums[:i]
        l2 = nums[i:]
        l3 = l2 + l1
        for i in range(n):
            nums[i] = l3[i]