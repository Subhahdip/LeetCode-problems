class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        #print(s)
        slow = 0
        
        for i in range(len(s)):
            if s[i] == ' ' or i == len(s) - 1:
                if s[i] == ' ':
                    fast = i - 1
                else:
                    fast = i
                while slow < fast:
                    #print(slow, fast)
                    s[slow], s[fast] = s[fast], s[slow]
                    slow += 1
                    fast -= 1
                slow = i + 1
        
        return "".join(s)
                