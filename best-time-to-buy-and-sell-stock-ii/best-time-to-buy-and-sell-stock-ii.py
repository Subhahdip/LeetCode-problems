class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        s = 0
        for i in range(1, len(nums)):
            s += max(0,nums[i] - nums[i-1])
        return s