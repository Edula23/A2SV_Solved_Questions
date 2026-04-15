# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postIndex = {val: i for i, val in enumerate(postorder)}
        def build(preLeft, preRight, postLeft, postRight):
            if preLeft > preRight:
                return None
            root = TreeNode(preorder[preLeft])
            if preLeft == preRight:
                return root
            leftVal = preorder[preLeft + 1]
            mid = postIndex[leftVal]
            leftSize = mid - postLeft + 1
            root.left = build(preLeft + 1, preLeft + leftSize, postLeft, mid)
            root.right = build(preLeft + leftSize + 1, preRight, mid + 1, postRight-1)
            return root
        res = build(0, len(preorder)-1, 0, len(postorder)-1)
        return res