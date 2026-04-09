# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs_goodnode(node, max_ancestor) -> int:
            if not node: return 0

            count = 1 if node.val >= max_ancestor else 0
            max_ancestor = max(max_ancestor, node.val)
            return count + dfs_goodnode(node.left, max_ancestor) + dfs_goodnode(node.right, max_ancestor)
        
        return dfs_goodnode(root, float('-inf'))