# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _rightSideView_(self, root: Optional[TreeNode], h: int):
        if not root: return

        if h > self.h:
            self.ans.append(root.val)
            self.h += 1
        self._rightSideView_(root.right, h + 1)
        self._rightSideView_(root.left, h + 1)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        self.h = 0
        self.ans = []
        
        self._rightSideView_(root, 1)

        return self.ans