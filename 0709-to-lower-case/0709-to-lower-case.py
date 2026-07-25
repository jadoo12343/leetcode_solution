class Solution:
    def toLowerCase(self, s: str) -> str:
        st=""
        for k in s:
            if k in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                st+=k.lower()
            else:
                st+=k
        return st

        