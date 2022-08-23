# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return n
        
        left = 1
        right = n
        
        
        while left<=right:
            mid = (left+right)//2
            
            if isBadVersion(mid):
                
                if isBadVersion(mid-1):
                    right = mid - 1
                
                else:
                    return mid
            
            else:
                left = mid + 1