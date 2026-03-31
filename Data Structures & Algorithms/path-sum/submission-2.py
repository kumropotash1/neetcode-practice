# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False

        def hps(node, currentSum: int):
            nonlocal targetSum
            currentSum += node.val
            if not (node.left or node.right):
                return currentSum == targetSum
            
            hasleftpathsum = hps(node.left, currentSum) if node.left else False
            hasrightpathsum = hps(node.right, currentSum) if node.right else False

            return hasleftpathsum or hasrightpathsum
        return hps(root, 0)
