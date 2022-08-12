class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        c = 0;
        while n:
            tmp = n // 5
            c += tmp
            n = tmp
        
        return c