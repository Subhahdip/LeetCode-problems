class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        i = 0
        
        count = 0;
 

        for i in range(0, n):
            if (arr[i] != 0):
                arr[count] = arr[i]
                count+=1

        for i in range(count, n):
            arr[i] = 0
            
        return arr