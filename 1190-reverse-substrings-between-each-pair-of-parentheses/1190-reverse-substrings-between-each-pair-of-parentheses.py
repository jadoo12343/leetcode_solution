class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = [""]
        for i in s:
            if i == "(":
                st.append("")
            elif i == ")":
                temp = st.pop()
                st[-1] += temp[::-1]
            else:
                st[-1]+=i
        return st[-1]
