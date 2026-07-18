class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        rev=0
        if x<0:
            return False
        while num!=0:
            rev=rev*10+num%10
            num=num//10
        return rev==x
        
