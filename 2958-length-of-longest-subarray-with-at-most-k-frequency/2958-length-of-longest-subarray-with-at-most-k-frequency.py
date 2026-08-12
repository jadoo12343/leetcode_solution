class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        over = 0
        freq = {}
        l = 0
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            if freq[n] == k + 1:
                over += 1
            if over > 0:
                freq[nums[l]] -= 1
                if freq[nums[l]] == k:
                    over -= 1
                l += 1
        return len(nums) - l