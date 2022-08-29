# Runtime: 53 ms, faster than 77.96% of Python3 online submissions for Path Sum.
# Memory Usage: 15 MB, less than 56.89% of Python3 online submissions for Path Sum.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        return self.recurse(root,targetSum,0)
        
    def recurse(self,node,target,sum_above):
        if node.left is None and node.right is None:
            return (sum_above + node.val)  == target
        left_success = False if node.left is None else self.recurse(node.left,target,sum_above+node.val)
        right_success = False if node.right is None else self.recurse(node.right,target,sum_above+node.val)
        return left_success or right_success