class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        count = 0
        while (i*(i+1))//2 <= n :
            i+=1
            count +=1
        return count 

        
        