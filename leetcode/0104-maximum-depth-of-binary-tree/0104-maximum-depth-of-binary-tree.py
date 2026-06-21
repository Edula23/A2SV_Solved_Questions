# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return 0
        def trav(root, n):
            nonlocal res
            if not root.left and not root.right:
                res = max(res, n)
            if root.left:
                trav(root.left, n+1)
            if root.right:
                trav(root.right, n+1)
            return
        trav(root, 1)
        return res