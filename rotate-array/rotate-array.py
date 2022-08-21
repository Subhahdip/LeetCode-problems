class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseArray( arr, start, end):
            while (start < end):

                    arr[start], arr[end] = arr[end], arr[start]
                    start = start + 1
                    end = end - 1


        def rightRotate( arr, d, n):

                reverseArray(arr, 0, n - 1);
                reverseArray(arr, 0, d - 1);
                reverseArray(arr, d, n - 1);
        
        
        
        if k > len(nums):
            k = k % len(nums)

        rightRotate(nums, k, len(nums))
            
            