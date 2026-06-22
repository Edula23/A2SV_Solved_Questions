# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def helper(root):
            nonlocal res
            if not root:
                return (float('inf'), float('-inf'))
            if not root.left and not root.right:
                return (root.val, root.val)
            
            left = helper(root.left)
            right = helper(root.right)
            
            print(left, right)

            minn = min(left[0], right[0])
            maxx = max(left[1], right[1])

            res = max(res, abs(root.val-minn), abs(root.val-maxx))

            minn = min(minn, root.val)
            maxx = max(maxx, root.val)
            return (minn, maxx)


        helper(root)
        return res
        