class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = len)
        
        s = strs[0]
        
        for i in strs:
            
            temp = ''
            for j in range(len(s)):
                
                if s[j] == i[j]:
                    temp+= s[j]
                
                else:
                    s = temp
                    break
                    

        return s
            