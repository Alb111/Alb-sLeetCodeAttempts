# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    preorder: list[int] = []
    inorder: list[int] = []
    poi: int = 0
    val_to_index: dict[int, int] = {}

    def build_tree_recursive(self, left: int, right: int) -> TreeNode:
        if left > right:
            return None

        node_to_add: TreeNode = TreeNode(self.preorder[self.poi])
        index_of_slipt: int = self.val_to_index[self.preorder[self.poi]]

        self.poi += 1

        node_to_add.left = self.build_tree_recursive(left, index_of_slipt - 1)
        node_to_add.right = self.build_tree_recursive(index_of_slipt + 1, right)

        return node_to_add

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # hashin
        self.preorder = preorder
        self.inorder = inorder
        for i, val in enumerate(inorder):
            self.val_to_index[val] = i

        return self.build_tree_recursive(0,len(inorder)-1)
        







