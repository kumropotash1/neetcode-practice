# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _levelOrder_(self, root: Optional[TreeNode], h: int):
        if not root: return

        if len(self.ans) < h:
            self.ans.append([])
        self.ans[h - 1].append(root.val)

        self._levelOrder_(root.left, h + 1)
        self._levelOrder_(root.right, h + 1)
            
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        self.ans = []
        self._levelOrder_(root, 1)

        return self.ans
