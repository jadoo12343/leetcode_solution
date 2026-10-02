class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(n):
            newnum = 0
            while n :
                digit = n%10
                newnum += digit**2
                n = n//10
            return newnum
        slow = next_num(n)
        fast = next_num(next_num(n))
        while slow != fast:
            if fast == 1:
                return True
            slow = next_num(slow)
            fast = next_num(next_num(fast))
        return slow==1
                


