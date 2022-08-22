class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        buffer = {}
        
        for i in range(len(nums)):
            
            if nums[i] not in buffer:
                buffer[target - nums[i]] = i 
            else:
                return [buffer[nums[i]], i]