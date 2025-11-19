# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def depth_recursive(self, root: TreeNode, layer: int) -> int:
        if root is None:
            return layer
        else:
            left_subtree: int = self.depth_recursive(root.left, layer + 1)
            right_subtree: int = self.depth_recursive(root.right, layer + 1)
            return max(left_subtree, right_subtree)
            
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth_recursive(root, 0)


