class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        sum=0
        if len(arr)<3:
            return True
        else:
            for i in range(len(arr)-2):
                if arr[i]-arr[i+1]==arr[i+1]-arr[i+2] or arr[i+1]-arr[i]==arr[i+2]-arr[i+1]:
                    sum+=1
            return sum==len(arr)-2