class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        end = -1
        
        for i in range(len(nums)):
            if nums[i] == target and start == -1:
                start = i
                end = i
            elif start is not -1 and nums[i] == target:
                end += 1
                
            elif nums[i] > target:
                break
                
        return [start, end]