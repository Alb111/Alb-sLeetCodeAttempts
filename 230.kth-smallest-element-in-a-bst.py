# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    curr_val: int = -1
    n: int = 0
    def in_order_traverse(self, root: TreeNode, k: int) -> None:
        if root is None:
            return
        else:
            self.in_order_traverse(root.left, k)

            # do work here
            self.n += 1
            if self.n == k:
                self.curr_val = root.val
                return

            self.in_order_traverse(root.right, k)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.in_order_traverse(root, k)
        return self.curr_val
