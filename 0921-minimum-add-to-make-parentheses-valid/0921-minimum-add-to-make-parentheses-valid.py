class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = []
        count = 0
        for i in s:
            if i == "(":
                res.append("(")
            else:
                if not res:
                    count +=1
                else:
                    temp = res.pop()
        return count + len(res)