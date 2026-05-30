# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = TreeNode()
        if q.val > p.val:
            less = p.val
            high = q.val
        else:
            less = q.val
            high = p.val
        def dfs(root):
            # print(root.val)
            if not root:
                return
            if less <= root.val <= high:                
                res.val = root.val
                return root
            dfs(root.left)
            dfs(root.right)
            return
        dfs(root)
        return res

            
            
            

            