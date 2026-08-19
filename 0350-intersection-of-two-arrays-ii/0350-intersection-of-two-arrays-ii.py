class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums1)
        m=len(nums2)
        res=[]
        if n>=m:
            for i in nums1:
                if i in nums2:
                    res.append(i)
                    nums2.remove(i)
        else:
            for i in nums2:
                if i in nums1:
                    res.append(i)
                    nums1.remove(i)
        return res
            
        