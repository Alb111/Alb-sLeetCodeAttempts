# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:           
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: TreeNode) -> tuple[int, bool]:
            if root is None:
                return (0, True)         
            else:
                left: tuple[int, bool] = dfs(root.left)
                right: tuple[int, bool] = dfs(root.right)

                if left[1] and right[1] and abs(left[0]-right[0]) <= 1:
                    return (1 + max(left[0], right[0]), True)
                else:
                    return (1 + max(left[0], right[0]), False)

        return dfs(root)[1]
                    



