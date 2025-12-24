# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def add_to_levels(self, root: TreeNode, levels: [list[int]], level: int) -> None:
        if root is None:
            return level 
        else:
            levels[level].append(root.val) 
            return max(self.add_to_levels(root.left, levels, level+1), self.add_to_levels(root.right, levels, level+1))

    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        levels: list[list[int]] = [[] for i in range(1000)]
        max_level: int = self.add_to_levels(root, levels, 0)
        right_side: list[int] = [levels[i][-1] for i in range(max_level)] 
        return right_side

        
