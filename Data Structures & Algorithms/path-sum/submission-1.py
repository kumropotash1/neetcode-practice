# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        def helper(node, currentSum):
            nonlocal targetSum
            currentSum += node.val
            if not (node.left or node.right):
                return currentSum == targetSum
            return (helper(node.left, currentSum) if node.left else False) or (helper(node.right, currentSum) if node.right else False)

        return helper(root, 0)