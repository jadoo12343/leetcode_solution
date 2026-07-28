class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff=high-low
        n=low%2
        m=high%2
        if n==0 and m==0:
            return (diff)//2
        if n!=0 and m!=0:
            return (diff)//2 + 1
        else:
            return (diff+1)//2
