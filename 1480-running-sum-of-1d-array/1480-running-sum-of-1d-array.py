class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev = 0
        for i in range(len(nums)):
            nums[i] = prev + nums[i]
            prev = nums[i]
            
        return nums