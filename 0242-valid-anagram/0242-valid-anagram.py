class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        sum1=0
        if n==m:
            for i in s :
                if s.count(i)==t.count(i):
                    sum1+=1
        return sum1==len(s)
        

                
    