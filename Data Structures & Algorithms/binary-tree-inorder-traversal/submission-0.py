# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _traverse_(self, node: Optional[TreeNode]):
        if not node: return

        self._traverse_(node.left)
        self.l.append(node.val)
        self._traverse_(node.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        self.l = []

        self._traverse_(root)

        return self.l
        