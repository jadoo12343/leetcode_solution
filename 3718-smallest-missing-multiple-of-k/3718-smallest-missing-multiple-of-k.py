class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        res=k
        s = set(nums)
        while res in s:
            res+=k
        return res
        