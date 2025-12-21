# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def checkForSubtree(self, subtree: TreeNode, nodeToCheck: TreeNode):
        if subtree is None and nodeToCheck is None:
            return True
        else:
            if subtree is None or nodeToCheck is None:
                return False
            elif subtree.val != nodeToCheck.val:
                return False
            else:
                return self.checkForSubtree(subtree.left, nodeToCheck.left) and self.checkForSubtree(subtree.right, nodeToCheck.right) 

                            
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        else:
            if self.checkForSubtree(subRoot, root):
                return True
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

            

        
