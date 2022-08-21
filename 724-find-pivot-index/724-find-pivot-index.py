class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        s = sum(nums)
        prev = 0
        for i in range(len(nums)):
            if s - nums[i] - prev == prev:
                return i
            prev += nums[i]
        
        return -1