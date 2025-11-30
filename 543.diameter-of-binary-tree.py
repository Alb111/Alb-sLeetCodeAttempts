# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_diameter = 0    

    def height(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left_side: int = self.height( root.left)
            right_side: int = self.height(root.right)
            found_diamater: int = left_side + right_side
            self.max_diameter = max(found_diamater, self.max_diameter)
            return 1 + max(self.height(root.left), self.height(root.right)) 

            
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # base case
        self.height(root)
        return self.max_diameter
