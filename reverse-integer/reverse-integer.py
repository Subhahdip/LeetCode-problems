class Solution:
    def reverse(self, x: int) -> int:
        s = list(str(x))
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != '-':
                s[i], s[j] = s[j], s[i]
                i+=1
                j-=1
            else:
                i+=1
                
        
        n = int("".join(s))
        
        if abs(n) < 2**31 - 1:
            return n
        return 0