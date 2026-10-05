class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        n = len(t)
        sp, tp = 0, 0
        while tp < n:
            if t[tp] == s[sp]:
                sp += 1
                if sp == len(s):
                    return True
            tp += 1   
        return False