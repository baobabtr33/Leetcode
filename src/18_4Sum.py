class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        ret = set()
        # sort
        nums = sorted(nums)
        # iterate through with 2 outer nums
        # 2 inner nums use hi, lo that matches inner_loop_target value
        for outer in range(len(nums)-3):
            for outer_1 in range(outer+1, len(nums)-2): 
                loop_target = target - nums[outer] - nums[outer_1]
                hi = len(nums)-1
                lo = outer_1+1
                while lo < hi:
                    _sum = nums[lo] + nums[hi]
                    if _sum == loop_target:
                        ret.add((nums[outer], nums[outer_1], nums[lo], nums[hi]))
                        hi -= 1
                        lo += 1
                    elif _sum > loop_target:
                        hi -= 1
                    else:
                        lo += 1
                        
        return list(ret)
