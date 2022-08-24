class Solution:
    def generate(self, n: int) -> List[List[int]]:
        triangle = [[1]]
        
        
        for _ in range(n - 1):
            temp = [1]
            for i in range(1, len(triangle[-1])):
                temp.append(triangle[-1][i-1] + triangle[-1][i])
            temp.append(1)
            triangle.append(temp)
            
        return triangle