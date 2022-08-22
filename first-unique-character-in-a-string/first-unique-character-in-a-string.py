class Solution:
    def firstUniqChar(self, s: str) -> int:
        buffer  = {}
        for i in range(len(s)):
            if s[i] in buffer:
                buffer[s[i]] += 1
            else:
                buffer[s[i]] = 1
        for i in range(len(s)):
            if buffer[s[i]] == 1:
                return i
        return -1