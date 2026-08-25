class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        l = 1
        h = n//2
        if n == 1:
            return 1
        if n == 3:
            return 2
        while l <= h:
            mid = (l+h)//2
            if (mid*(mid+1))//2 <= n:
                ans = mid
                l = mid+1
            else:
                h = mid-1
        return ans

        
        