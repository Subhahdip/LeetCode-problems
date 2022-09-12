class Solution:
    def partitionString(self, s: str) -> int:
        c = 1
        temp = ''
        for i in s:
            if i in temp:
                c += 1
                temp = ' '
            temp += i
        return c