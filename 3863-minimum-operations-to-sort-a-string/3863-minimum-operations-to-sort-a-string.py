class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 2 and sorted(s) != list(s):
            return -1
        
        if sorted(s) == list(s):
            return 0

        mn = min(s)
        mx = max(s)
        first = s[0]
        last = s[-1]

        if first == mn or last == mx:
            return 1

        # need to get the last to the front
        if first == mx and last == mn:
            if s.count(mn) > 1 or s.count(mx) > 1:
                return 2
            return 3
        
        return 2