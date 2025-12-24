# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def count_good_nodes(self, root: TreeNode, max_found: int) -> int:
        if root is None:
            return 0
        else:
            if max_found <= root.val:
                max_found = root.val
                return 1 + self.count_good_nodes(root.left, max_found) + self.count_good_nodes(root.right, max_found)
            else:
                return self.count_good_nodes(root.left, max_found) + self.count_good_nodes(root.right, max_found)

    def goodNodes(self, root: TreeNode) -> int:
        return self.count_good_nodes(root, -9999)
        
