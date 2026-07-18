class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = ""
        for i in range(len(x)):
            y = x[i] + y
        if y == x:
            return True
        else:
            return False
