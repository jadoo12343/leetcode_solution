class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        n=len(nums)
        seen=[]
        for i in range(n):
            if nums[i] not in seen:
                seen.append(nums[i])
                k+=1
            else:
                nums[i]=100
        nums.sort()
        return k 
        return nums
                

        