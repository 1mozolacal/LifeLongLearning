# Runtime: 56 ms, faster than 19.59% of Python3 online submissions for Same Tree.
# Memory Usage: 14 MB, less than 60.76% of Python3 online submissions for Same Tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        return self.same(p,q)

    def same(self,a,b):
        if (a is None and b is None):
            return True
        elif (not a is None and not b is None):
            if not a.val == b.val:
                return False
        else:
            return False

        right_side = self.same(a.right,b.right)
        left_side = self.same(a.left,b.left)
        
        return right_side and left_side
             
        