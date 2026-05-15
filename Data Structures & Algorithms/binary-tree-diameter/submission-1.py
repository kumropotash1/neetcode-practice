# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        cache = {}

        def _height_(root: Optional[TreeNode]):
            if not root: return 0
            if not root in cache:
                cache[root] = 1 + max(_height_(root.left), _height_(root.right))
            return cache[root]
        
        ans = 0

        def dfs(root: Optional[TreeNode]):
            if not root: return

            left_height = _height_(root.left)
            right_height = _height_(root.right)

            nonlocal ans
            ans = max(ans, left_height + right_height)

            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ans
        
        