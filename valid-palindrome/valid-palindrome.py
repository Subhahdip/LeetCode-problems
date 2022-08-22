class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        temp = []
        for i in range(len(s)):
            if s[i].isalnum():
                temp.append(s[i].lower())
        
        
        return temp == temp[::-1]
            