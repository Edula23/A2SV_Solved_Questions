# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node, p, gp):
            if not node:
                return 0
            total = 0
            if gp and gp.val % 2 == 0:
                total += node.val
            total += dfs(node.left, node, p)
            total += dfs(node.right, node, p)

            return total
        return dfs(root, None, None)



            