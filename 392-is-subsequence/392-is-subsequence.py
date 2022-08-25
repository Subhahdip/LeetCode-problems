class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        
        for _ in t:
            
            if i == len(s):
                break
            
            if _ == s[i]:
                i += 1
        return i == len(s)