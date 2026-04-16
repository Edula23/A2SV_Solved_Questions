# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def dfs(root):
            nonlocal ans 
            if not root:
                return 0
            val = root.val
            left = dfs(root.left)
            right = dfs(root.right)
            ans = max(ans, val, val + left, val + right, val + left + right)
            return max(val, val + left, val + right)
        dfs(root)
        return ans