# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _kthSmallest(self, node: Optional[TreeNode]):
        if not node: return
        if not self.k: return

        self._kthSmallest(node.left)
        self.k -= 1
        if self.k == 0:
            self.ans = node.val
            return
        self._kthSmallest(node.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self._kthSmallest(root)
        return self.ans