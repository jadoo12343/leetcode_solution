# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    temp = None

    def flatten(self, root):
        self.helper(root)

    def helper(self, root):
        if root is None:
            return

        left = root.left
        right = root.right

        if self.temp is not None:
            self.temp.right = root

        root.left = None
        self.temp = root

        self.helper(left)
        self.helper(right)
        