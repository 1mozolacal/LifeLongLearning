import math
import re

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        return self.depth_finder(root,0)

    def depth_finder(self,list,depth):
        if list == None:
            return depth
        return max(self.depth_finder(list.left,depth+1),self.depth_finder(list.right,depth+1) )