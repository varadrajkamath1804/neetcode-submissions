class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n= len(heights)-1
        left=0
        right=n
        max_area=0

        while left < right:
            length=min(heights[left],heights[right])
            breadth=n
            area=length*breadth
            if area>max_area:
                max_area=area
            if heights[left]<heights[right]:
                left+=1
            elif heights[right]<=heights[left]:
                right-=1
            n-=1
        return max_area
            
            


        