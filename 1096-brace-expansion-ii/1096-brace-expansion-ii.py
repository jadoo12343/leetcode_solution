class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
            res = set()
            def dfs(s):
                if "{" not in s:
                    res.add(s)
                    return
                
                right = s.find("}")
                left = s.rfind("{",0,right)
                
                prefix = s[:left]
                choices = s[left + 1:right].split(",")
                suffix = s[right+1:]

                for choice in choices:
                    new_s = prefix + choice + suffix
                    dfs(new_s)
            dfs(expression)
            return sorted(res)

