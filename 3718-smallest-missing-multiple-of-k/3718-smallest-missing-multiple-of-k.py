class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        res=k
        while res in nums:
            res+=k
        return res
        