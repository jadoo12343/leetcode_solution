class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        str1=[]
        for i in s:
            if i not in str1:
                str1.append(i)
                res=max(res,len(str1))
            else:
                res=max(res,len(str1))
                k=str1.index(i)
                str1=str1[k+1:]
                str1.append(i)
        return res


