class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        series = [0,1,1]
        c = 1
        a = 0
        d = 0
        if n%2!=0:
            return False
        else:
            n = n/2
            while d < n :
                d = c + a
                a = c
                c = d
            return d == n

                

        
