class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = dict(knowledge)
        res , l = [] , 0
        while l < len(s):
            if s[l] == '(':
                r = s.find(')', l+1)
                res.append(d.get(s[l + 1 : r], '?'))
                l = r
            else:
                res.append(s[l])
            l +=1
        return "".join(res)
        