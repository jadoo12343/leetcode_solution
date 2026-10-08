class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st = []
        lis = []
        l , r = 0 ,0
        for i in s:
            if i== "(":
                l +=1
                st.append(i)
            else:
                r +=1
                st.append(i)
            if r == l:
                st.pop()
                st.pop(0)
                lis += st
                st = []
        return "".join(lis)

            

                
            