
#Returns the Maximum Depth of Binary Tree

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class solution(object):
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root== None: return 0
        if root.right==None and root.left==None: return 1
        def recMaxDepth(root: Optional[TreeNode]) -> int:
            if root==None: return 0

            if root.right==None and root.left==None: return 1
            
            return 1 + max(recMaxDepth(root.left),recMaxDepth(root.right))
        
        return 1 + max(recMaxDepth(root.left),recMaxDepth(root.right))
