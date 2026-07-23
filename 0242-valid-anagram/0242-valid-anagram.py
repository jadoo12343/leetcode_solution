class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sum1=0
        for i in s :
            if s.count(i)==t.count(i) and len(s)==len(t):
                sum1+=1
        return sum1==len(s)
        

                
    