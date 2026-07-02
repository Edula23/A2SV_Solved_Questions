# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []
        def dfs(root, arr):
            if not root:
                return
            if root and not root.left and not root.right:
                arr.append(root.val)
                return
            dfs(root.left, arr)
            dfs(root.right, arr)
        dfs(root1, tree1)
        dfs(root2, tree2)
        return True if tree1 == tree2 else False
            
            