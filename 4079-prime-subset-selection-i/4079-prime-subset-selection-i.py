class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        i = 1
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        res = []
        total_sum = 0
        for x in range(2,n+1):
            if is_prime[x]:
                if total_sum + x > s :
                    break
                total_sum+=x
                res.append(x)
        return res
                

        
                     
            
                

            