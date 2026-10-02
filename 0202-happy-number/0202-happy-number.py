class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1 and n not in seen:
            sum=0
            seen.add(n)
            while(n!=0):
                r=n%10
                sum=sum+r**2
                n=n//10
            n=sum
        return n==1


