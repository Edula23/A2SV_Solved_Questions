# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def traverse(curr, n):
            nonlocal res
            if not curr:
                res = max(res, n)
                return
            else:
                traverse(curr.left, n+1)
                traverse(curr.right, n+1)
        traverse(root, 0)
        return res