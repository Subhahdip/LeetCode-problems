class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        flag = True
        
        for i in range(len(nums) - 2, -1, -1):
            if flag == False:
                if nums[i] + i > index:
                    flag = True
            
            elif nums[i] == 0:
                flag = False
                index = i
        
        return flag
            