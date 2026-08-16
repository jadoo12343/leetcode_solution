class Solution:
    def maxArea(self, height: List[int]) -> int:
        self.height=height
        max_height=max(height)
        right=len(height)-1
        left=0
        ans = 0
        while left<right:
            area=(right-left)*min(height[left],height[right])
            if area>ans:
                ans=area
            if height[left]<height[right]:
                left +=1
            else:
                right -=1

            if (max_height * (right - left)) <= ans:
                break
            
                        
        return ans



        



        

                    


                


            

               