# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        order = []
        if root == None:
            return []
        self.traver(root, order)
        return order

    def traver(self, node, order_list):
        order_list.append(node.val)
        if not node.left == None:
            self.traver(node.left, order_list)
        if not node.right == None:
            self.traver(node.right, order_list)
