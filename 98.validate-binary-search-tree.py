# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValid(self, root: TreeNode, max_v: int, min_v: int) -> bool:
        if root is None:
            return True
        else:
            valid: bool = True 
            if root.left and (root.left.val >= root.val or root.left.val <= min_v):
                valid = False 
        
            if root.right and (root.right.val <= root.val or  root.right.val >= max_v):
                valid = False 

            return valid and self.isValid(root.left, root.val, min_v) and self.isValid(root.right, max_v, root.val)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, 1001, -1001)
