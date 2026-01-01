# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    max_sum = -1000001 # the minumum pos sum - 1
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def find_max(root: TreeNode) -> int:
            if root is None:
                return 0

            # find the sums at a node and update max 
            left: int = find_max(root.left)
            right: int = find_max(root.right)
            sum_with_vertex: int = root.val + left + right
            sum_without_vertex: int = root.val + max(0, left, right)
                        
            self.max_sum = max(self.max_sum, max(sum_with_vertex, sum_without_vertex))

            # return up path_sum without a vertex for parent node calc
            return sum_without_vertex

        find_max(root)
        return self.max_sum

        


            


