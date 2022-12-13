#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        
        checker = N//2
            
        A.sort()
        
        
        for i in range(N):
            if i + checker >= N:
                return -1
            if A[i] == A[i + checker]:
                return A[i]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends