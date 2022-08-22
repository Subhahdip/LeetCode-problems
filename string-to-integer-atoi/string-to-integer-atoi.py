class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.strip()
        t = ''
        
        
        if s == '':
            return 0
        
        

        
        if s[0] == '-' or s[0] == '+':
            t+=s[0]
        
            for i in range(1,len(s)):
                if s[i].isdigit():
                    t+=s[i]
                else:
                    break
        else:
            for i in range(len(s)):
                if s[i].isdigit():
                    t+=s[i]
                else:
                    break
        
        if t == '' or t == '+' or t == '-':
            return 0
        
        
        
        t = int(t)
        if t > 2**31 - 1:
            t = 2**31 - 1
        elif t < 0 - 2**31:
            t = 0 - 2**31
        return t
            