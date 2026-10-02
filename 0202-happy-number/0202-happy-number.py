class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1 and n not in seen:
            count = 0
            seen.add(n)
            while n!=0:
                digit = n%10
                count += digit**2
                n = n//10
            n = count
        return n==1


        