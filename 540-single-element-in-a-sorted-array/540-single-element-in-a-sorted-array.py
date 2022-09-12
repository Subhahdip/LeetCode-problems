class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 2
        
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == nums[mid^1]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]