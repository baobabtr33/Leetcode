class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1  
        ret = 0
        
        while left < right:
            if height[left] >= height[right]:
                ret = max(ret, (right - left) * height[right])
                right -= 1
            else:
                ret = max(ret, (right - left) * height[left])
                left += 1
                
        return ret
