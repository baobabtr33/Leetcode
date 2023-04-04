class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        
        for i in range(len(nums)-2):
            left = i+1
            if nums[i] == nums[i-1] and i > 0:
                continue
            right = len(nums) -1
            
            while left < right:
                _sum = nums[i] + nums[left] + nums[right]
                
                if _sum == 0:
                    ret.append([nums[i], nums[left], nums[right]])
                    # look ahead
                    while nums[left] == nums[left+1] and left < right-1:
                        left += 1 
                    while nums[right] == nums[right-1] and right > left + 1:
                        right -= 1
                    left += 1
                    right -= 1

                if _sum < 0:
                    left += 1
                elif _sum > 0: 
                    right -= 1
                
        return ret
