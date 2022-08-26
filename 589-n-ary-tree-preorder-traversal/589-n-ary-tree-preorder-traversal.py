"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        def dfs(root, output):

            if root is None:
                return

            output.append(root.val)

            for child in root.children:
                dfs(child, output)
        
        
        output =[]
        
        dfs(root, output)
        
        return output
    
        