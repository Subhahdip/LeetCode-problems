class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        while n > 2:
            c = a + b
            a = b
            b = c
            n -= 1
            
        return c