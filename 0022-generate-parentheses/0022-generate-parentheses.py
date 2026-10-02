class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n==1:
            return ["()"]
        res = []

        def dfs(a, b, c):
            if not a and not b:
                res.append(c + ")")
                return

            if a > 0:
                dfs(a - 1,b, c + "(")

            if b >= a:
                dfs(a, b - 1, c + ")")

        dfs(n-1, n-1, "(")

        return res