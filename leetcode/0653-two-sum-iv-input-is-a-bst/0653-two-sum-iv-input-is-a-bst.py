# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(node, ans):
            if not node:
                return False
            if k - node.val in ans:
                return True
            
            ans.add(node.val)
            return dfs(node.left, ans) or dfs(node.right, ans)
        ans = set()
        return dfs(root, ans)
        
