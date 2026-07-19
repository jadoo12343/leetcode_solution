class Solution:
    def romanToInt(self, s: str) -> int:
        values={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        N=len(s)
        index=0
        result=0
        while index < N:
            char=s[index]
            value=values[char]
            if index+1<N:
                nex_char=s[index+1]
                nex_value=values[nex_char]
                if value<nex_value:
                    result+=(nex_value-value)
                    index+=1
                else:
                    result+=value
            else:
                result+=value
                index+=1
            index+=1

        return result
            

        
        