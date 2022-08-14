class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0:
            return False
        
        stack = []
        
        for i in s:
            if i  == '{' or i == '(' or i == '[':
                stack.append(i)
            
            elif i == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            
            elif i == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
                
            elif i == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
        
        return not stack