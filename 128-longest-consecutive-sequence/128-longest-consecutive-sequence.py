class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxstreak = 0
        s = set(nums)
        
        for i in nums:
            
            if i - 1 not in s:
                curnum = i
                curstreak = 1
                
                while curnum + 1 in s:
                    curnum += 1
                    curstreak += 1
                
                maxstreak = max(maxstreak, curstreak)
                
        return maxstreak